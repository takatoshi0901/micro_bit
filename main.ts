input.onButtonPressed(Button.A, function () {
    Display = Display / 2
})
input.onGesture(Gesture.Shake, function () {
    Display = 1
})
input.onButtonPressed(Button.AB, function () {
    Display = input.compassHeading()
})
input.onButtonPressed(Button.B, function () {
    Display = Display * 2
})
let Display = 0
Display = 1
basic.forever(function () {
    basic.showNumber(Display)
})
