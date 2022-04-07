import torch


def main():
    x = torch.ones(2, 2, requires_grad=True)
    #print(x)
    #print(x.grad_fn)
    y = x + 2
    print(y)
    print(y.grad_fn)


if __name__ == '__main__':
    main()