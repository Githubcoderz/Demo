package Demoproject;



import java.net.MalformedURLException;

import java.net.URI;

import java.net.URL;



import org.openqa.selenium.remote.DesiredCapabilities;



import io.appium.java_client.android.AndroidDriver;
import io.appium.java_client.android.AndroidElement;



public class APKinstall {



	public static void main(String[] args) throws MalformedURLException {

		// TODO Auto-generated method stub

		//gather  desired capabilities

		

		DesiredCapabilities capabilities= new DesiredCapabilities();

		capabilities.setCapability("Appium:deviceName", "1830264510BA0C0J");

		capabilities.setCapability("Appium:platformName", "Android");

		capabilities.setCapability("Appium:automationName", "uiautomator2");

		capabilities.setCapability("Appium:app", "C:\\Users\\mishr\\Desktop\\WORKSPACE\\APKfiles\\testapp.apk");

		capabilities.setCapability("Appium:platformVersion","11");

		

		URL url = URI.create("http://127.0.0.1:4723/wd/hub").toURL();

		

		AndroidDriver <AndroidElement> driver = new AndroidDriver<>(url,capabilities);

		System.out.println("Application started");

		

		driver.quit();

		

	}



}