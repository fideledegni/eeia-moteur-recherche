const singleton = {};
const services = {};

singleton.register = (serviceName, vm) => {
  if (services[serviceName]) {
    throw new Error(`Singleton '${serviceName}' already exists!`);
  }
  services[serviceName] = vm;
};

singleton.exists = serviceName => services[serviceName];

singleton.get = serviceName => {
  const tmp = services[serviceName];
  if (!tmp) {
    throw new Error(`Service '${serviceName}' is not registered!`);
  }
  return tmp;
};

export default singleton;
