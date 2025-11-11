Deploy with ```kubectl create deployment todoapp-dep --image=roslinmahmud/todo-app```

Deploy with Manifest
```kubectl apply -f manifests/deployment.yaml```

Forward port with
```kubectl port-forward todoapp-dep-8974bd77f-pnlr2 8000:8000```