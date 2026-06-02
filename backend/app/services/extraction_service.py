from tika import parser
import os


# Extract raw text from a PDF or DOCX file using Apache Tika
def extract_text_from_file(file_path: str) -> str:
    # Tika parses the file and returns metadata + content
    try:
        parsed = parser.from_file(file_path)
    except Exception as e:
        # Surface a clearer, actionable error message when Tika fails to start
        msg = (
            "Tika server failed to start or could not be contacted. "
            "Ensure Java (JRE/JDK) is installed and available on PATH, then either: "
            "(1) run a Tika server jar with `java -jar tika-server.jar -p 9998` or "
            "(2) run the official Docker image `docker run -p 9998:9998 apache/tika:latest`. "
            "After starting the server, set the `TIKA_SERVER_ENDPOINT` environment variable to "
            "http://localhost:9998 or set `TIKA_SERVER_JAR` to the tika-server jar path. "
            "You can also pass `serverEndpoint='http://host:port'` to `parser.from_file`. "
            f"Underlying error: {e}"
        )
        raise RuntimeError(msg) from e

    content = parsed.get("content", "")

    # Clean up None values and whitespace
    if not content:
        return ""

    return content.strip()


# Get the file extension for basic validation
def get_file_extension(filename: str) -> str:
    return os.path.splitext(filename)[1].lower()