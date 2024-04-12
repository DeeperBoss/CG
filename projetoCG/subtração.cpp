#include <fstream>
#include <string>
#include <stdexcept>

using namespace std;

class Pixel {
public:
    int r, g, b;

    Pixel() : r(0), g(0), b(0) {}
    Pixel(int r, int g, int b) : r(r), g(g), b(b) {}

    Pixel operator+(Pixel &other) {
        return Pixel(r + other.r, g + other.g, b + other.b);
    }

    Pixel operator-(Pixel &other) {
        return Pixel(r - other.r, g - other.g, b - other.b);
    }

    string tostring() {
        return to_string(r) + " " + to_string(g) + " " + to_string(b);
    }
};

class PPMImage {
public:
    int width, height, maxColor;
    Pixel **pixels;

    PPMImage(int width, int height, int maxColor) : width(width), height(height), maxColor(maxColor) {
        pixels = new Pixel *[height];
        for (int i = 0; i < height; i++)
            pixels[i] = new Pixel[width];
    }

    PPMImage(string path) {
        ifstream file(path);
        if (!file.is_open())
            throw invalid_argument("Error: Could not open file " + path);

        string format;
        file >> format;
        if (format != "P3")
            throw invalid_argument("Error: Invalid file format");

        file >> width >> height >> maxColor;

        pixels = new Pixel *[height];
        for (int i = 0; i < height; i++)
            pixels[i] = new Pixel[width];

        for (int i = 0; i < height; i++)
            for (int j = 0; j < width; j++)
                file >> pixels[i][j].r >> pixels[i][j].g >> pixels[i][j].b;

        file.close();
    }

    ~PPMImage() {
        for (int i = 0; i < height; i++)
            delete[] pixels[i];
        delete[] pixels;
    }

    PPMImage operator-(PPMImage &other) {
        if (width != other.width || height != other.height)
            throw invalid_argument("Error: Can't subtract images of different dimensions");

        PPMImage newImage(width, height, maxColor);
        for (int i = 0; i < height; i++)
            for (int j = 0; j < width; j++)
                newImage.pixels[i][j] = pixels[i][j] - other.pixels[i][j];

        return newImage;
    }

    void normalize() {
        int max = 0;
        for (int i = 0; i < height; i++)
            for (int j = 0; j < width; j++)
                if (pixels[i][j].r > max)
                    max = pixels[i][j].r;

        for (int i = 0; i < height; i++)
            for (int j = 0; j < width; j++)
                pixels[i][j] = Pixel(pixels[i][j].r * 255 / max, pixels[i][j].g * 255 / max, pixels[i][j].b * 255 / max);
    }

    void segment() {
        for (int i = 0; i < height; i++)
            for (int j = 0; j < width; j++)
                if (pixels[i][j].r > 0)
                    pixels[i][j] = Pixel(255, 255, 255);
                else
                    pixels[i][j] = Pixel(0, 0, 0);
    }

    void save(string path) {
        ofstream file(path);
        file << "P3\n" << width << " " << height << "\n" << maxColor << "\n";
        for (int i = 0; i < height; i++)
            for (int j = 0; j < width; j++)
                file << pixels[i][j].tostring() << " ";
        file.close();
    }
};

int main() {
    PPMImage image1("detecção/foto1.ppm");
    PPMImage image2("detecção/foto2.ppm");

    PPMImage subtractedImage = image1 - image2;
    subtractedImage.normalize();
    subtractedImage.save("detecção/normalizada.ppm");

    PPMImage segmentedImage = subtractedImage;
    segmentedImage.segment();
    segmentedImage.save("detecção/segmentada.ppm");

    return 0;
}