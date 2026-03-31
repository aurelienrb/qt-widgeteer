from widgeteer_client import Response, SyncWidgeteerClient
import base64
import sys
import time
import pyautogui
# pip install pyautogui websockets

def test_screenshot(client):
    r = client.screenshot(annotate=True)
    #print(r)
    if r.success:
        print("Saving screenshot to file")
        image_data = base64.b64decode(r.value)
        with open("screenshot.png", "wb") as f:
            f.write(image_data)


def test_service_call(client):
    #print(client.list_services())
    r = client.call_service(service="myService", method="add", args=["a", 2])
    if r.success:
        print(f"Result: {r.value}")
    else:
        print(f"Error: {r.error}")


def set_text(client: SyncWidgeteerClient, target: str, text: str) -> Response:
    r = client.invoke(target=target, method="clear")
    if not r.success:
        return r
    return client.input_text(target=target, text=text)

def main():
    with SyncWidgeteerClient(port=9000) as client:
        #r = client.command("show_context_menu")
        #r = client.right_click("#nameEdit")
        #r = client.focus(target="#mainWindow")
        #assert r.success

        #r = client.find("#nameEdit")
        #assert r.success and r.data["count"] == 1
        r = client.describe("#mainWindow")
        assert r.success
        print(r.data)
        x = int(r.data["globalPosition"]["x"])
        y = int(r.data["globalPosition"]["y"])
        print(f"click at {x}, {y}")
        pyautogui.moveTo(x, y)
        #assert r.success

    return 0
#    result = client.find("@class:QPushButton")
#    for match in result.data.get("matches", []):
#        print(f"{match['objectName']}: {match['path']}")

if __name__ == '__main__':
    sys.exit(main())
