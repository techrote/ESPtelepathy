#include <stddef.h>
#include <stdint.h>
#include <stdio.h>

#include "esp_app_desc.h"
#include "project_identity.h"

static void bytes_to_hex(const uint8_t *input, size_t input_length, char *output)
{
    static const char hex_digits[] = "0123456789abcdef";

    for (size_t index = 0; index < input_length; ++index) {
        output[index * 2] = hex_digits[input[index] >> 4];
        output[index * 2 + 1] = hex_digits[input[index] & 0x0f];
    }
    output[input_length * 2] = '\0';
}

void app_main(void)
{
    const esp_app_desc_t *app = esp_app_get_description();
    char elf_sha256[(sizeof(app->app_elf_sha256) * 2) + 1];
    bytes_to_hex(app->app_elf_sha256, sizeof(app->app_elf_sha256), elf_sha256);

    printf(
        ESPTELEPATHY_IDENTITY_PREFIX
        "{\"record\":\"identity\","
        "\"project\":\"ESPtelepathy\","
        "\"project_version\":\"%s\","
        "\"git_sha\":\"%s\","
        "\"idf_version\":\"%s\","
        "\"telemetry_schema\":\"%s\","
        "\"target\":\"%s\","
        "\"build_config\":\"%s\","
        "\"elf_sha256\":\"%s\","
        "\"build_date\":\"%s\","
        "\"build_time\":\"%s\"}\n",
        app->version,
        ESPTELEPATHY_GIT_SHA,
        app->idf_ver,
        ESPTELEPATHY_TELEMETRY_SCHEMA_VERSION,
        ESPTELEPATHY_BUILD_TARGET,
        ESPTELEPATHY_BUILD_CONFIG_ID,
        elf_sha256,
        app->date,
        app->time);
}
