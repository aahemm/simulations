# Mininet simulations
Run the run.py's run() function for getting best assignment.
 
For running the best assignment in Mininet you should run multipleControlers.py in a machine with Mininet installed.  

# Kubernetes
To run kubernetes deployment simply run "kubectl create -f odlcontroller.YAML" and then "kubectl create -f odlcontroller-svc.YAML" on a master machine with kubernetes installed. Then you can access the cluster from port 6633.
