const { HAND_CONNECTIONS, drawConnectors, drawLandmarks, lerp } = window;

export class Mirror {
    constructor({ video, canvas, context, landmarkGrid }) {
        this.video = video;
        this.canvas = canvas;
        this.context = context;
        this.landmarkGrid = landmarkGrid;
    }

    updateGrid(multiHandedness, multiHandWorldLandmarks) {
        if (multiHandedness.length > 0) {
            this.landmarkGrid.updateLandmarks(
                [...multiHandWorldLandmarks[0]],
                HAND_CONNECTIONS,
                [
                    {
                        list: [...Array(HAND_CONNECTIONS.length).keys()],
                        color: multiHandedness[0].label,
                    },
                ],
            );
        } else {
            this.landmarkGrid.updateLandmarks([]);
        }
    }

    drawHandLandmarks(multiHandLandmarks, multiHandedness) {
        multiHandLandmarks.forEach((landmarks, index) => {
            const { label } = multiHandedness[index];
            const rightHand = label === "Right";

            const color = rightHand ? "#00FF00" : "#FF0000";
            const fillColor = rightHand ? "#FF0000" : "#00FF00";

            drawConnectors(this.context, landmarks, HAND_CONNECTIONS, {
                color,
                lineWidth: 2,
            });

            drawLandmarks(this.context, landmarks, {
                color,
                fillColor,
                lineWidth: 2,
                radius: (data) => lerp(data.from.z, -0.15, 0.1, 10, 1),
            });
        });
    }

    loadMirrored(image) {
        const aspectRatio = this.video.videoHeight / this.video.videoWidth;
        const greaterInnerWidth = window.innerWidth > window.innerHeight;

        const width = greaterInnerWidth
            ? window.innerHeight / aspectRatio
            : window.innerWidth;
        const height = greaterInnerWidth
            ? window.innerHeight
            : window.innerWidth * aspectRatio;

        this.canvas.width = width;
        this.canvas.height = height;

        this.context.save();
        this.context.clearRect(0, 0, this.canvas.width, this.canvas.height);
        this.context.drawImage(
            image,
            0,
            0,
            this.canvas.width,
            this.canvas.height,
        );
    }
}
