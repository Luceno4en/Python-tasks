import json
import os
from http.server import HTTPServer, BaseHTTPRequestHandler

def main():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r", encoding="utf-8") as f:
            tasks = json.load(f)
    else:
        tasks = []

    next_id = max((t["id"] for t in tasks), default=0) + 1

    def save_tasks():
        with open("tasks.txt", "w", encoding="utf-8") as f:
            json.dump(tasks, f, ensure_ascii=False)

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            if self.path == "/tasks":
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(tasks, ensure_ascii=False).encode())
            else:
                self.send_response(404)
                self.end_headers()

        def do_POST(self):
            nonlocal next_id
            if self.path == "/tasks":
                content_len = int(self.headers.get("Content-Length", 0))
                data = json.loads(self.rfile.read(content_len).decode())
                task = {
                    "id": next_id,
                    "title": data["title"],
                    "priority": data["priority"],
                    "isDone": False
                }
                tasks.append(task)
                next_id += 1
                save_tasks()
                self.send_response(201)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(task, ensure_ascii=False).encode())

            elif "/tasks/" in self.path and self.path.endswith("/complete"):
                try:
                    parts = self.path.strip("/").split("/")
                    if len(parts) == 3 and parts[2] == "complete":
                        task_id = int(parts[1])
                        for t in tasks:
                            if t["id"] == task_id:
                                t["isDone"] = True
                                save_tasks()
                                self.send_response(200)
                                self.end_headers()
                                return
                    self.send_response(404)
                except (ValueError, IndexError):
                    self.send_response(404)
                self.end_headers()
            else:
                self.send_response(404)
                self.end_headers()

    print("Сервер запущен: http://localhost:8000")
    server = HTTPServer(("localhost", 8000), Handler)
    server.serve_forever()

if __name__ == '__main__':
    main()