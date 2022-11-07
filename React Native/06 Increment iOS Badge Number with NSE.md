# Increment iOS Badge Number with NSE

## Tutorials

1. [LogRocket - Creating React Native badge components in iOS](https://blog.logrocket.com/creating-react-native-badge-components-ios/#badge-manager-React-Native)
1. [STRV - App Extensions: Introduction to Notification Service](https://www.strv.com/blog/app-extensions-introduction-to-notification-service-engineering)
1. [WonderPush - Adding a Notification Service Extension](https://docs.wonderpush.com/docs/adding-a-notification-service-extension)
1. [ChenJoyqul - 用 Notification Service Extension 去做自動新增 badge count](https://joyqul.medium.com/%E7%94%A8-notification-service-extension-%E5%8E%BB%E5%81%9A%E8%87%AA%E5%8B%95%E6%96%B0%E5%A2%9E-badge-count-2b4b3e265fa0)
1. [Marta - How to debug iOS Notification Service Extension](https://medium.com/tiendeo-tech/how-to-debug-ios-extension-d8841f998db4)

## Apple Documentations

1. [UNNotificationServiceExtension](https://developer.apple.com/documentation/usernotifications/unnotificationserviceextension)
1. [UserDefaults](https://developer.apple.com/documentation/foundation/userdefaults)
1. [Configuring App Groups](https://developer.apple.com/documentation/xcode/configuring-app-groups)
1. [Configuring a new target in your project](https://developer.apple.com/documentation/xcode/configuring-a-new-target-in-your-project)
1. [Adding capabilities to your app](https://developer.apple.com/documentation/xcode/adding-capabilities-to-your-app#Add-a-capability)
1. [Modifying Content in Newly Delivered Notifications](https://developer.apple.com/documentation/usernotifications/modifying_content_in_newly_delivered_notifications)

## Steps

1. Add `UserDefaults` to store badge count
1. Add `NotificationServiceExtension` to modify remote notification
1. Add `{ mutable-content: 1 }` to notification payload
1. Manipulate the badge count on `AppDelegate.m`
1. Manipulate the badge number on `NotificationService.swift`
1. Update the deployment target of `NotificationServiceExtension`
