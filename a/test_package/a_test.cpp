#include <acme/a.hpp>

int main(int argc, const char * * argv) {
    acme::a::Apple apple;
    return 42 == apple.count() ? 0 : 1;
}
