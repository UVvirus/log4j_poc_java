package com.example;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import java.util.Scanner;

public class LoggerApp {
    private static final Logger logger = LogManager.getLogger(LoggerApp.class);
    private static final Logger userAgentLogger = LogManager.getLogger("UserAgentLogger");
    public static void main(String[] args) {
    if (args.length < 2) {
        System.out.println("Please provide two numbers as command line arguments.");
        return;
    }

    String num1 = args[0];
    String num2 = args[1];

    String result = addNumbers(num1, num2);
    logger.info("Result of addNumbers function: {}", result);
    // Get the user agent
    String userAgent = System.getProperty("http.agent");
    userAgentLogger.info("User Agent: {}", userAgent);
    logger.info("LoggerApp finished");
}
    public static String addNumbers(String a, String b) {
        logger.info("addNumbers function called with arguments: {}, {}", a, b);
        return a + b;
}}
