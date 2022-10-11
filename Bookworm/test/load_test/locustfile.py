from locust import HttpUser, task

sample_data = [53734, 20163, 49240, 1889, 57171]

class APITest(HttpUser):
    @task
    def user_info(self):
        for user_id in sample_data:
            self.client.get("/user_recoms/{user_id}", name="/user")