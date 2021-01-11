from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(1, 10)

    @task
    def index(self):
        self.client.get("/api/v1/countries")
