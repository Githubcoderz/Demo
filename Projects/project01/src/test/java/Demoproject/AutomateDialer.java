package Demoproject;

import java.net.MalformedURLException;
import java.net.URI;
import java.net.URL;

import org.openqa.selenium.By;

import org.openqa.selenium.remote.DesiredCapabilities;

import io.appium.java_client.android.AndroidDriver;
import io.appium.java_client.android.AndroidElement;

public class AutomateDialer {

	public static void main(String[] args) throws MalformedURLException, InterruptedException {
		// TODO Auto-generated method stub
		
		DesiredCapabilities capabilities= new DesiredCapabilities();

		capabilities.setCapability("deviceName", "1830264510BA0C0J");

		capabilities.setCapability("platformName", "Android");

		capabilities.setCapability("automationName", "uiautomator2");

		capabilities.setCapability("platformVersion","11");

		capabilities.setCapability("appPackage", "com.google.android.dialer");
		
		capabilities.setCapability("appActivity", "com.google.android.dialer.extensions.GoogleDialtactsActivity");

		URL url = URI.create("http://127.0.0.1:4723/").toURL();

		
		AndroidDriver <AndroidElement>  driver = new AndroidDriver<>(url,capabilities);

		
		
		System.out.println("Application started");

		
		//click Dial pad 
		driver.findElement(By.id("com.google.android.dialer:id/dialpad_fab")).click();
		
		//dial key number
	
		driver.findElement(By.id("com.google.android.dialer:id/one")).click();
		driver.findElement(By.id("com.google.android.dialer:id/two")).click();
		driver.findElement(By.id("com.google.android.dialer:id/one")).click();
		
		//com.google.android.dialer:id/dialpad_voice_call_button

		driver.findElement(By.id("com.google.android.dialer:id/dialpad_voice_call_button")).click();
		 
		Thread.sleep(5000);
	
		
		driver.quit();

	}

}
