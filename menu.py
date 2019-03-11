from requester import RequesterToSpaceX
from formatters import SpaceXFormatter


def main():
    while True:
        urls = {
            1: 'https://api.spacexdata.com/v3/launches/next',
            2: 'https://api.spacexdata.com/v3/launches/latest',
            3: 'https://api.spacexdata.com/v3/launches/upcoming',
            4: 'https://api.spacexdata.com/v3/launches/past'
        }

        formatter = SpaceXFormatter()

        for k, v in urls.items():
            print(f'[{k}] - {v.split("/")[-1]}')

        option = int(input('Informe a opção de consulta: '))
        requester = RequesterToSpaceX(urls.get(option))
        request = requester.get_request()

        if option > 2:
            # It should iterate, because the response for upcoming and past
            # launches return a list of dicts.
            for item in request:
                print(formatter.format_response(item))
        else:
            print(formatter.format_response(request))


if __name__ == '__main__':
    main()
