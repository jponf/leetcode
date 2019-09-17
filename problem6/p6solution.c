#include <stdlib.h>
#include <stdio.h>
#include <string.h>


char* convert(const char* str, int n_rows)
{
    size_t i, j, n_middle_rows = n_rows - 1;
    size_t cycle = 2 * n_rows - 2;

    size_t str_len = strlen(str);
    char* out = (char*)malloc((str_len + 1) * sizeof(char));
    char* cursor = out;

    if (n_rows <= 1) {
        strcpy(out, str);
    } else {
        out[str_len] = '\0';

        // first row
        for (j = 0; j < str_len; j += cycle) {
            *(cursor++) = str[j];
        }

        // middle rows
        for (i = 1; i < n_middle_rows; ++i) {
            for (j = 0; i + j < str_len; j+= cycle) {
                *(cursor++) = str[j + i];
                if (j + cycle - i < str_len) {
                    *(cursor++) = str[j + cycle - i];
                }
            }
        }

        // last row
        for (j = n_rows - 1; j < str_len; j += cycle) {
            *(cursor++) = str[j];
        }
    }

    return out;
}


int main(int argc, char** argv)
{
    const char* original = "PAYPALISHIRING";
    const int num_rows = 4;

    char* out = convert(original, num_rows);
    printf("Original: %s\n", original);
    printf("Zig Zag (# rows %d): %s\n", num_rows, out);

    free(out);

    return EXIT_SUCCESS;
}