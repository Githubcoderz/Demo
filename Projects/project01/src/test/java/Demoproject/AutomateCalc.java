package Demoproject;

import java.net.MalformedURLException;
import java.net.URI;
import java.net.URL;

import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.remote.DesiredCapabilities;

import io.appium.java_client.android.AndroidDriver;
import io.appium.java_client.android.AndroidElement;

public class AutomateCalc {

	public static void main(String[] args) throws MalformedURLException {
		// TODO Auto-generated method stub
		
		//gather  desired capabilities

		

				DesiredCapabilities capabilities= new DesiredCapabilities();

				capabilities.setCapability("deviceName", "1830264510BA0C0J");

				capabilities.setCapability("platformName", "Android");

				capabilities.setCapability("automationName", "uiautomator2");

				capabilities.setCapability("platformVersion","11");

				capabilities.setCapability("appPackage", "com.google.android.calculator");
				
				capabilities.setCapability("appActivity", "com.android.calculator2.Calculator");

				URL url = URI.create("http://127.0.0.1:4723/").toURL();

				
				AndroidDriver <AndroidElement>  driver = new AndroidDriver<>(url,capabilities);

				
				
				System.out.println("Application started");

				
				//click numbers
				WebElement num5 = driver.findElement(By.id("com.google.android.calculator:id/digit_5"));
				num5.click();
				
				WebElement plus = driver.findElement(By.id("com.google.android.calculator:id/op_add"));
				plus.click();
				
				WebElement num6 = driver.findElement(By.id("com.google.android.calculator:id/digit_6"));
				num6.click();
				
				
				//result
				WebElement resultPreview = driver.findElement(By.id("com.google.android.calculator:id/result_preview"));
				String resultString =resultPreview.getText();
				if(resultString.equals("11"))
				{
					System.out.println("PASS");
				}
				else
				{
					System.out.println("FAIL");
				}
				

				driver.quit();

		
	}

}
