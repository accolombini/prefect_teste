from prefect import flow


@flow(name="hello-world")
def hello_world():
    print("Olá, Prefect 2.x em execução!")


if __name__ == "__main__":
    hello_world()
