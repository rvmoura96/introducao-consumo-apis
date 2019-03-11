from abc import ABC, abstractmethod


class AbstractFormatter(ABC):
    """Abstract class to extends to specific inputs."""

    @abstractmethod
    def format_response(self, json: dict) -> None:
        """Abstract format response."""
        pass


class SpaceXFormatter(AbstractFormatter):
    """Extension from AbstractFormatter to format SpaceX responses."""

    def format_response(self, json: dict) -> str:
        """Format SpaceX dicts from responses."""
        response = (
            f'Número do voo: {json.get("flight_number")}\n'
            f'Missão: {json.get("mission_name")}\n'
            f'Ano de Lançemento: {json.get("launch_year")}\n'
            f'Data de lançamento: {json.get("launch_date_utc")}\n'
        )

        return response
