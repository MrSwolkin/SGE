import csv
from django.core.management.base import BaseCommand
from brands.models import Brand


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            "file_name",
            type=str,
            help="nome do arquivo com marcas"
        )

    def handle(self, *args, **options):
        print(f"argumentos recebidos {options}")
        file_name = options["file_name"]

        try:
            with open(file_name, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    name = row["name"]
                    description = row["description"]

                    Brand.objects.create(
                        name=name,
                        description=description
                    )
                    self.stdout.write(self.style.NOTICE(f"{name} adicionado com sucesso"))

            self.stdout.write(self.style.SUCCESS(f"arquivo {file_name}, importado com sucesso"))
        except FileNotFoundError:
            self.stderr.write(self.style.ERROR(f"Arquivo '{file_name}' não encontrado."))
        except KeyError as e:
            self.stderr.write(self.style.ERROR(f"Coluna ausente no CSV: {e}"))
