#ifndef __SUP_DEBUG__
#define __SUP_DEBUG__

#include <stdio.h>

#define SUP_DEBUG // Enable debug. Comment out to disable.

// Setup debug printing macros.
#ifdef SUP_DEBUG

#define SUP_DEBUG_PRINT(...)                                                   \
  { printf(__VA_ARGS__); }

// define a macro that return same string if debug is active or NULL if not
#define SUP_DEBUG_STR(...) __VA_ARGS__

#else

#define SUP_DEBUG_PRINT(...)

#define SUP_DEBUG_STR(...) NULL

#endif
#endif // __SUP_DEBUG__