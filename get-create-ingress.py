from kubernetes import client, config

def create_ingress(networking_v1_api):
    body = client.V1Ingress(
        api_version="networking.k8s.io/v1",
        kind="Ingress",
        metadata=client.V1ObjectMeta(name="my-ingress", annotations={
            "nginx.ingress.kubernetes.io/rewrite-target": "/"
        }),
        spec=client.V1IngressSpec(
            rules=[client.V1IngressRule(
                host="example.com",
                http=client.V1HTTPIngressRuleValue(
                    paths=[client.V1HTTPIngressPath(
                        path="/",
                        path_type="Exact",
                        backend=client.V1IngressBackend(
                            service=client.V1IngressServiceBackend(
                                port=client.V1ServiceBackendPort(
                                    number=5678,
                                ),
                                name="service-example")
                            )
                    )]
                )
            )
            ]
        )
    )
    networking_v1_api.create_namespaced_ingress(
        namespace="default",
        body=body
    )


def main():
    config.load_kube_config()
    apps_v1_api = client.AppsV1Api()
    networking_v1_api = client.NetworkingV1Api()

    create_ingress(networking_v1_api)


if __name__ == "__main__":
    main()