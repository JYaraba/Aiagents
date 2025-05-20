from aiagents.base.base_agent import BaseAgent
from aiagents.utils.file_writer import write_output_file
from aiagents.utils.progress_tracker import log_progress_step

class JavaDeveloperAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="JavaDeveloperAgent",
            role="Java Backend Developer",
            goal="Generate Java backend code using Spring Boot structure",
            backstory="Expert in building backend logic using Java, Spring Boot, and REST APIs for scalable applications."
        )

    @log_progress_step("JavaDeveloperAgent", "Generating Java backend logic")
    def execute(self, task_data: list | dict) -> dict:
        # Generate simple REST controller
        controller_code = """package com.example.todo;

import org.springframework.web.bind.annotation.*;
import java.util.ArrayList;
import java.util.List;

@RestController
@RequestMapping("/todos")
public class TodoController {
    private final List<String> todos = new ArrayList<>();

    @GetMapping
    public List<String> getTodos() {
        return todos;
    }

    @PostMapping
    public String addTodo(@RequestBody String task) {
        todos.add(task);
        return "Task added successfully.";
    }
}
"""
        # Generate main app
        app_code = """package com.example.todo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class TodoApplication {
    public static void main(String[] args) {
        SpringApplication.run(TodoApplication.class, args);
    }
}
"""
        write_output_file("output/src/main/java/com/example/todo/TodoController.java", controller_code)
        write_output_file("output/src/main/java/com/example/todo/TodoApplication.java", app_code)

        return {
            "status": "executed",
            "agent": self.name,
            "details": "Generated Java Spring Boot backend files."
        }
