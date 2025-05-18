from aiagents.base.base_agent import BaseAgent
from aiagents.utils.progress_tracker import log_progress_step
from aiagents.utils.file_writer import write_java_file


class JavaDeveloperAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="JavaDeveloperAgent", role="Java Backend Developer")

    @log_progress_step("JavaDeveloperAgent", "Generating Java Spring Boot boilerplate")
    def execute(self, prompt: str) -> dict:
        """
        Generates basic Java Spring Boot backend structure based on the prompt.
        Includes: Main application class and a simple controller.
        """
        java_main_code = """\
package com.aiagents.app;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class AiagentsApplication {
    public static void main(String[] args) {
        SpringApplication.run(AiagentsApplication.class, args);
    }
}
"""

        controller_code = """\
package com.aiagents.app.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloController {

    @GetMapping("/api/hello")
    public String hello() {
        return "Hello from AI-generated Java backend!";
    }
}
"""

        files = {
            "output/server/src/main/java/com/aiagents/app/AiagentsApplication.java": java_main_code,
            "output/server/src/main/java/com/aiagents/app/controller/HelloController.java": controller_code,
        }

        for path, content in files.items():
            write_java_file(path, content)

        self.remember("java_files", list(files.keys()))
        return {"generated_files": list(files.keys())}
