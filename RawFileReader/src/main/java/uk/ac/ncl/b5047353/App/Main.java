package uk.ac.ncl.b5047353.App;

import java.io.*;
import java.sql.Timestamp;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.UUID;

import org.apache.commons.lang3.math.NumberUtils;
import org.jdom2.Document;
import org.jdom2.Element;
import org.jdom2.JDOMException;
import org.jdom2.input.SAXBuilder;


/**
 * Created by mbax2nk2 on 29/05/2016.
 */
public class Main {
    private static String currentDirection;
    private static String uniqueID = "##-nursultan-##";
    private static String finalLine = "";
    private static ArrayList<String> errors = new ArrayList<>();
    public static void main(String[] args) {
        int noOfFolders;
        File[] files = null;
        String currentDir = System.getProperty("user.dir");

        File dir = new File("results");
        File currentFolder = new File(System.getProperty("user.dir"));
        File[] folders = currentFolder.listFiles(new FileFilter() {
            @Override
            public boolean accept(File pathname) {
                return pathname.isDirectory();
            }
        });
        files = new File[folders.length];
        if (dir.mkdir()) {
            System.out.println("Results will be stored in results folder");
        } else {
            System.out.println("Cannot create folder results");
        }
        for (int i = 0; i < folders.length; i++) {
            files[i] = new File(currentDir + "/run" + i + "/SPECjvm2008.001.raw");
            System.out.print("-");
            try {
                finalLine = "";
                finalLine += uniqueID;
                currentDirection = "run" + UUID.randomUUID().toString();;
                SAXBuilder saxBuilder = new SAXBuilder();

                Document document = saxBuilder.build(files[i]);

                Element classElement = document.getRootElement();

                List<Element> benchmarkList = classElement.getChildren();

                for (Element benchmark : benchmarkList) {
                    saveEntry(benchmark);
                    if (benchmark.getChildren() != null) {
                        getChildren(benchmark.getChildren());
                    }
                }
                writeToCSV(finalLine);
            } catch (JDOMException | IOException e) {
                errors.add(files[i].getAbsolutePath() + " file structure is not complete");
            }
        }
        System.out.println();
        if (errors.size() > 0) {
            System.out.println("Errors found in:");
            for (String error : errors) {
                if (error != null)
                    System.out.println(error);
            }
        }
        System.out.println("Completed");


    }

    private static void getChildren(List<Element> benchmarkList) {
        for (Element benchmark : benchmarkList) {
            saveEntry(benchmark);
            if (benchmark.getChildren() != null) {
                getChildren(benchmark.getChildren());
            }
        }
    }

    private static void saveEntry(Element element) {
        String parent = element.getParent().toString().replaceAll("[\\[</>\\]]", "").replace("Element: ", "").trim();
        String elementName = element.getName();
        double operations;
        double operationsPerMinute;
        long duration;
        switch (elementName) {
            case "spec.jvm2008.report.run.location":
                writeToCSV(element.getName() + "=" + element.getValue());
                finalLine += "," + element.getValue();
                writeToCSV(System.getProperty("line.separator"));
                break;
            case "spec.jvm2008.report.hw.cpu.name":
                writeToCSV(element.getName() + "=" + element.getValue().trim());
                if(!element.getValue().trim().isEmpty()){
                    finalLine += "," + element.getValue().trim();
                }else{
                    finalLine += ",n/a";
                }
                writeToCSV(System.getProperty("line.separator"));
                break;
            case "spec.jvm2008.report.hw.memory.size":
                writeToCSV(element.getName() + "=" + element.getValue().trim());
                if(NumberUtils.isNumber(element.getValue().trim())){
                    finalLine += "," + element.getValue().trim();
                }else{
                    finalLine += ",n/a";
                }
                writeToCSV(System.getProperty("line.separator"));
                break;
            case "spec.jvm2008.report.hw.number.of.cores":
                writeToCSV(element.getName() + "=" + element.getValue().trim());
                if(NumberUtils.isNumber(element.getValue().trim())){
                    finalLine += "," + element.getValue().trim();
                }else{
                    finalLine += ",n/a";
                }
                writeToCSV(System.getProperty("line.separator"));
                break;
            case "benchmark-result":
                writeToCSV("benchmark-name=" + element.getAttributeValue("name") + ", ");
                finalLine += "," + element.getAttributeValue("name") + ",";
                break;
            case "error":
                errors.add(currentDirection+".csv "+element.getValue());
                break;
            case "iteration-result":
                operations = Double.parseDouble(element.getAttributeValue("operations"));
                Date startTime = new Date(Long.parseLong(element.getAttributeValue("startTime")));
                Date endTime = new Date(Long.parseLong(element.getAttributeValue("endTime")));
                duration = endTime.getTime() - startTime.getTime();
                if (parent.equals("iterations")) {
                    if (operations == 1.0) {
                        operationsPerMinute = ((double) 240000 / duration) / 4;

                    } else {
                        operationsPerMinute = operations / 4.0;
                    }
                    writeToCSV("mode=normal, start=" + startTime.toString() + ", end="
                            + endTime.toString() + ", " + "operations=" + operations
                            + ", operationsPerMinute=" + Double.parseDouble(Double.toString(operationsPerMinute)));
                    finalLine += startTime.toString() + "," + endTime.toString() + "," + operations
                            + "," + Double.parseDouble(Double.toString(operationsPerMinute));
                    writeToCSV(System.getProperty("line.separator"));
                } else {
                    operationsPerMinute = operations / 2.0;
                    writeToCSV("mod=warmup, start=" + startTime.toString() + ", end="
                            + endTime.toString() + ", " + "operations=" + operations
                            + ", operationsPerMinute=" + Double.parseDouble(Double.toString(operationsPerMinute)) + ", ");
                    finalLine += startTime.toString() + "," + endTime.toString() + ","+ operations +","+ Double.parseDouble(Double.toString(operationsPerMinute)) + ",";

                }
                break;
        }
    }

    private static void writeToCSV(String text) {
        try (PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("results/" + currentDirection + ".csv", true)))) {
            out.print(text);
            out.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

}
