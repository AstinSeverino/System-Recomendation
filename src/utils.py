import logging

def setup_logging():
    """
    Configura el logging básico.
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s:%(name)s: %(message)s"
    )
