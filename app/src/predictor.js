import { loadLayersModel, tensor3d } from "@tensorflow/tfjs";

const alphabet = [
    "A",
    "B",
    "C",
    "CH",
    "CZ",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "R",
    "RZ",
    "S",
    "SZ",
    "T",
    "U",
    "W",
    "Y",
    "Z",
    "Ó",
    "Ą",
    "Ć",
    "Ę",
    "Ł",
    "Ń",
    "Ś",
    "Ź",
    "Ż",
];

export class Predictor {
    constructor() {
        this.sequences = [];
        this.sign = "";
        this.accuracy = 0;
    }

    async init() {
        try {
            this.model = await loadLayersModel("model.json");

            this.predict = this.throttle(500);
        } catch (error) {
            console.error(error);
        }
    }

    shiftSequences(multiHandedness, multiHandWorldLandmarks) {
        const enoughFrames = this.sequences.length === 30;

        if (enoughFrames) this.sequences.shift();

        const rightHandIndex = this.getRightHandIndex(multiHandedness);
        const landmarks =
            rightHandIndex !== -1
                ? multiHandWorldLandmarks[rightHandIndex]
                : [];
        const sequence = landmarks
            .map((landmark) => [landmark.x, landmark.y, landmark.z])
            .flat();

        this.sequences.push(sequence);

        const noneEmpty = this.sequences.every(
            (sequence) => sequence.length === 63,
        );

        if (!enoughFrames || !noneEmpty) return;

        this.predict(0.9);
    }

    throttle(delay) {
        this.predictionTime = Date.now();

        return (threshold) => {
            let now = Date.now();

            if (now - this.predictionTime > delay) {
                this.predictionTime = now;

                const tensor = this.model.predict(tensor3d([this.sequences]));
                const [predictions] = tensor.arraySync();
                const topAccuracy = Math.max(...predictions);
                const prediction = alphabet[predictions.indexOf(topAccuracy)];

                if (topAccuracy >= threshold) {
                    this.sign = prediction;
                    this.accuracy = topAccuracy;
                }
            }
        };
    }

    getRightHandIndex(multiHandedness) {
        return multiHandedness.findIndex(
            (handedness) => handedness.label === "Right",
        );
    }

    getSign() {
        return this.sign;
    }

    getAccuracy() {
        return this.accuracy;
    }
}
