#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <zip.h>

// Function to perform manipulation on each file in the zip archive
void manipulateFilesInZip(const std::string& zipFilename) {
    // Open the zip archive
    int err = 0;
    zip* archive = zip_open(zipFilename.c_str(), 0, &err);
    if (!archive) {
        std::cerr << "Failed to open zip file: " << zip_strerror(archive) << std::endl;
        return;
    }

    // Get the number of files in the archive
    int numFiles = zip_get_num_entries(archive, 0);

    // Iterate over each file in the archive
    for (int i = 0; i < numFiles; ++i) {
        // Open the file in the archive
        zip_file* file = zip_fopen_index(archive, i, 0);
        if (!file) {
            std::cerr << "Failed to open file " << i << " in zip: " << zip_strerror(archive) << std::endl;
            continue;
        }

        // Get the file name
        struct zip_stat fileStat;
        zip_stat_init(&fileStat);
        zip_stat_index(archive, i, 0, &fileStat);
        std::string filename = fileStat.name;

        // Read the file contents
        std::vector<char> buffer(fileStat.size);
        zip_fread(file, buffer.data(), fileStat.size);

        // Manipulate the file contents here
        // For example, you can modify the contents of 'buffer'

        // Close the file in the archive
        zip_fclose(file);
    }

    // Close the zip archive
    zip_close(archive);
}

int main() {
    std::string zipFilename = "example.zip";
    manipulateFilesInZip(zipFilename);
    return 0;
}
