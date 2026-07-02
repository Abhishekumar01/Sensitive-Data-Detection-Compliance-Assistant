"""Text Splitter Module
Splits extracted document text into smaller chunks for
LLM processing, embeddings, and vector databases."""

from langchain.text_splitter import RecursiveCharacterTextSplitter


def split_document(
    text,
    chunk_size=1000,
    chunk_overlap=200
):
    """
    Split a document into overlapping chunks.

    Parameters
    ----------
    text : str
        Extracted document text.

    chunk_size : int
        Maximum number of characters in each chunk.

    chunk_overlap : int
        Number of overlapping characters between chunks.

    Returns
    -------
    list
        List of text chunks.
    """

    if not text:
        return []

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=[
            "\n\n",
            "\n",
            ". ",
            " ",
            ""
        ]
    )

    chunks = splitter.split_text(text)

    return chunks