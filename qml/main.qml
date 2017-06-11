import QtQuick 2.7
import QtQuick.Window 2.2
import QtCharts 2.2

Window {
    visible: true
    title: qsTr("QML")
    width: img.width
    height: img.height
    Image{
        id: img
        source: "wtm3.png"
    }
}
