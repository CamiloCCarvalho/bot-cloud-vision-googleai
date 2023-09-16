from botcity.plugins.cloudvision import BotCloudVisionPlugin


def main():

    # Instantiate the plugin
    cloudvision = BotCloudVisionPlugin()


    # Setup the path to the service account key credentials JSON file
    cloudvision.credentials(fr"C:\Users\ash\Desktop\cloud_vision\cred.json")

    # Read the text from the image
    cloudvision.read("ottercrossing.png")

    # Print the text from the image
    print(cloudvision.full_text())

if __name__ == '__main__':
    main()
