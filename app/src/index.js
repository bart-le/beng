const { LandmarkGrid, Camera, Hands } = window;

import { Mirror } from "./mirror";
import { Predictor } from "./predictor";

const root = document.querySelector("#root");
const spinner = document.querySelector("#loading");
const grid = document.querySelector("#grid");
const letter = document.querySelector("#letter");
const meter = document.querySelector("#accuracy");
const label = document.querySelector("#bar label");
const video = document.querySelector("#video");
const canvas = document.querySelector("#mirror");
const context = canvas.getContext("2d");

const mirror = new Mirror({
    video,
    canvas,
    context,
    landmarkGrid: new LandmarkGrid(grid, {
        connectionColor: 0xcccccc,
        definedColors: [
            { name: "Right", value: "#00FF00" },
            { name: "Left", value: "#FF0000" },
        ],
        range: 0.2,
        fitToGrid: false,
        labelSuffix: "m",
        landmarkSize: 2,
        numCellsPerAxis: 3,
        showHidden: false,
        centered: true,
    }),
});

const predictor = new Predictor();

const resultsListener = ({
    image,
    multiHandLandmarks,
    multiHandWorldLandmarks,
    multiHandedness,
}) => {
    if (!canvas || !video || !context || !letter || !meter || !label) return;

    mirror.loadMirrored(image);

    if (
        !image ||
        !multiHandLandmarks ||
        !multiHandWorldLandmarks ||
        !multiHandedness
    )
        return;

    mirror.drawHandLandmarks(multiHandLandmarks, multiHandedness);
    mirror.updateGrid(multiHandedness, multiHandWorldLandmarks);

    predictor.shiftSequences(multiHandedness, multiHandWorldLandmarks);

    const rightHand = predictor.getRightHandIndex(multiHandedness) !== -1;
    const currentAccuracy = rightHand
        ? predictor.getAccuracy().toFixed(5)
        : null;

    letter.innerHTML = rightHand ? predictor.getSign() : "";
    label.innerHTML = currentAccuracy;
    meter.value = currentAccuracy;
};

const init = async () => {
    await predictor.init();

    spinner.ontransitionend = () => {
        spinner.style.display = "none";
    };

    const hands = new Hands({
        locateFile: (file) =>
            `https://cdn.jsdelivr.net/npm/@mediapipe/hands/${file}`,
    });

    hands.setOptions({
        selfieMode: true,
        maxNumHands: 1,
        modelComplexity: 1,
        minDetectionConfidence: 0.5,
        minTrackingConfidence: 0.5,
    });

    hands.onResults(resultsListener);

    const camera = new Camera(video, {
        onFrame: async () => {
            await hands.send({ image: video });

            root.classList.add("loaded");
        },
        facingMode: "user",
        width: 1280,
        height: 720,
    });

    camera.start();
};

document.addEventListener("DOMContentLoaded", () => {
    init();
});
