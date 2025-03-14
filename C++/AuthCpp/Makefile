SRCDIR = src
ROUTEDIR = routes
INCLUDEDIR = include
OBJDIR = obj

SRCS = $(wildcard $(SRCDIR)/*.cpp) $(wildcard $(ROUTEDIR)/*.cpp)
OBJS = $(patsubst %.cpp, $(OBJDIR)/%.o, $(SRCS))

CXX = g++
CXXFLAGS = -std=c++20 -Wall -I$(INCLUDEDIR)
LDFLAGS = -lpqxx -lpq -pthread -lboost_system -lboost_thread -lboost_filesystem -lboost_program_options -lssl -lcrypto

TARGET = app

all: $(TARGET)

$(TARGET): $(OBJS)
	$(CXX) $(CXXFLAGS) -o $(TARGET) $(OBJS) $(LDFLAGS)

# Crear directorios antes de compilar y mantener la estructura
$(OBJDIR)/%.o: %.cpp
	@mkdir -p $(dir $@)  # Crea la carpeta donde se guarda el .o
	$(CXX) $(CXXFLAGS) -c $< -o $@

# Ajustar las rutas de los archivos fuente para que coincidan con la regla de compilación
$(OBJDIR)/$(SRCDIR)/%.o: $(SRCDIR)/%.cpp
	@mkdir -p $(dir $@)
	$(CXX) $(CXXFLAGS) -c $< -o $@

$(OBJDIR)/$(ROUTEDIR)/%.o: $(ROUTEDIR)/%.cpp
	@mkdir -p $(dir $@)
	$(CXX) $(CXXFLAGS) -c $< -o $@

clean:
	rm -rf $(OBJDIR) $(TARGET)
