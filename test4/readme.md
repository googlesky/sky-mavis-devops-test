`helm install ingress-test --set domain=gw.skymavis.xyz,hosts[0].name=us,hosts[1].name=eu`

This will create an ingress resource with two host rules, one for `us.gw.skymavis.xyz` and one for `eu.gw.skymavis.xyz`, as well as a deployment and service for the nginx container. You can then use the following command to test the ingress paths:
`for i in us eu;do curl -L $i.gw.skymavis.xyz;done`

This should return the hostname for each host in the hosts list.