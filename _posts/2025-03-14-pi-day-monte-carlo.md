---
layout: post
title: "带派不老铁！从计算圆周率到蒙特卡罗"
date: 2026-03-14 12:00:00 +0800
---

## 引言：圆周率 与 Pi Day

每年的 $3$ 月 $14$ 日被称为 圆周率日（**Pi Day**），因为

$$
\pi \approx 3.14
$$

计算 $\pi$ 的方法有很多，例如几何法、无穷级数以及连分数等。中国古代数学家祖冲之就用割圆法（圆内接正多边形逼近的方法）计算出 $\pi$ 的范围是 $\frac{22}{7}<\pi<\frac{355}{113}$，即 $3.1415926$ 与 $3.1415927$ 之间。 

小学二年级时就学过泰勒级数(Taylor series)/麦克劳林级数(Maclaurin series)的你一定知道

$$
\arctan x = \sum\limits_{n=0}^\infty \frac{(-1)^n}{2n+1} x^{2n+1}
$$

于是注意到 $\arctan 1 = \frac{\pi}{4}$，即有

$$
\frac{\pi}{4}=\sum\limits_{n=0}^\infty \frac{(-1)^n}{2n+1}
$$

当然叻，还可以用Machin公式 $\frac{\pi}{4} = 4\arctan{\frac{1}{5}}-\arctan{\frac{1}{239}}$ 对上述展开加速。

大数学家欧拉(Euler)在1734年解决了巴塞尔问题，由此

$$\sum\limits_{n=1}^\infty \frac{1}{n^2}=\frac{\pi^2} {6}$$

也可以计算圆周率。

而如今应用最广、收敛速度最快的一类圆周率计算公式，则来自于注意力惊人的印度数学家 拉马努金（Ramanujan)！他注意到

$$
\frac{1}{\pi}
=
\frac{2\sqrt{2}}{9801}
\sum_{k=0}^{\infty}
\frac{(4k)!}{(k!)^4}
\frac{1103+26390k}{396^{4k}}
$$

你每计算一项，大约能增加8位精度。

在此基础上，1988 年，乌克兰数学家 David Chudnovsky 和 Gregory Chudnovsky 发现了更快的公式：

$$
\frac{1}{\pi}
=
12
\sum_{k=0}^{\infty}
\frac{(-1)^k (6k)!}{(3k)!(k!)^3}
\frac{13591409+545140134k}{640320^{3k+\frac{3}{2}}}
$$

这个公式的收敛速度更为惊人：每计算一项，约可以增加 $14$ 位精度。

但你可能会说了，这些级数都太难算了，我刚注册没多久的新号既不爱算数注意力又涣散，有没有什么闭着眼就能计算圆周率的方法呢？

有的孩子，有的。

这种方法看似非常反直觉：

*只使用随机数，我们就可以计算 $\pi$。*

但实际上是个人只要会闭眼会撒针那么就能算$\pi$。
这就是著名的 **蒙特卡罗(Monte Carlo) 方法**。Pi Day来闭眼算 $\pi$ 吧！

## 一个简单的 Monte Carlo 实验

考虑正方形

$$
[-1,1]^2
$$

在该正方形中均匀随机选择点 $(X,Y)$。我们关心事件

$$
X^2 + Y^2 \le 1,
$$

也就是点落在单位圆内。

由于

$$
\text{S(圆)} = \pi, \qquad
\text{S(正方形)} = 4,
$$

因此

$$
P(X^2 + Y^2 \le 1) = \frac{\pi}{4}.
$$

于是

$$
\pi = 4P(X^2 + Y^2 \le 1).
$$

如果生成 $N$ 个随机点，其中 $H$ 个落在圆内，则

$$
\pi \approx 4 \frac{H}{N}.
$$

这就是一个最简单的 Monte Carlo 估计。用大白话就是说蒙住眼睛的你随机往一个 $2\times 2$ 的正方形区域里投 $N$ 枚针，然后数出来有 $M$ 枚针落入了正方形内接圆内，然后算一下 $\frac{M}{N}$ 就是 $\pi$ 的近似值了。

## Python 示例：用 Monte Carlo 估计 $\pi$

下面给出一个简单的 Python 程序。它在正方形 $[-1,1]^2$ 中生成随机点，并统计落在单位圆内的比例。

```python
import random
import math
import matplotlib.pyplot as plt

random.seed(314)
N = 10000
xs_in, ys_in, xs_out, ys_out = [], [], [], []
hit = 0

for _ in range(N):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x*x + y*y <= 1:
        hit += 1
        xs_in.append(x)
        ys_in.append(y)
    else:
        xs_out.append(x)
        ys_out.append(y)

pi_est = 4 * hit / N
abs_err = abs(pi_est - math.pi)

print("N =", N)
print("Hits =", hit)
print("Estimated pi =", pi_est)
print("Absolute error =", abs_err)

fig, ax = plt.subplots(figsize=(5, 5))
ax.scatter(xs_in, ys_in, s=3, alpha=0.6, label="Inside circle")
ax.scatter(xs_out, ys_out, s=3, alpha=0.6, label="Outside circle")

circle = plt.Circle((0, 0), 1, fill=False)
ax.add_patch(circle)

ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect("equal", adjustable="box")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title(f"Monte Carlo estimation of pi (N={N}, estimate={pi_est:.6f})")
ax.legend()
fig.tight_layout()
fig.savefig("assets/monte_carlo_pi_plot.png", dpi=150, bbox_inches="tight")
```

本次运行中，取 $N=10000$，命中次数为 $H=7831$，因此

$$
\hat\pi = 4\frac{H}{N} = 3.132400.
$$

与真实值相比，绝对误差约为

$$
|\hat\pi - \pi| \approx 0.0092.
$$

下图展示了本次模拟的散点图。

![Monte Carlo 方法估计 π 的散点图](/assets/monte_carlo_pi_plot.png)

## 从几何到积分

上述概率可以写为积分形式：

$$
P(X^2+Y^2 \le 1)
=
\int_{[-1,1]^2}
1_{\{x^2+y^2\le1\}}\, d\mu
$$

其中 $\mu$ 是 随机变量 $(X, Y)$ 在$[-1, 1]^2$ 上诱导的分布测度，即

$$
\mu = P \circ (X,Y)^{-1}
$$

 $1_{\{x^2+y^2\le1\}}$ 是单位圆的指示函数。因此

$$
\pi
=
4 \int_{[-1,1]^2}
1_{\{x^2+y^2\le1\}}\, d\mu.
$$

也就是说，计算 $\pi$ 的问题本质上变成了计算一个积分。

但小学三年级时学习过多重积分的你可能会说了，不对啊，这和我学过的二重积分不一样啊？

恭喜你盲生，发现了华点！

这其实是一样的叻，

设 $(X,Y)$ 在正方形 $[-1,1]^2$ 上均匀分布。则其诱导的分布测度为

$$
\mu = \frac{ \lambda|_{[-1,1]^2}}{\lambda ([-1,1]^2)} = \frac{dy\, dx}{4}
$$

其中 $\lambda$ 为 Lebesgue 测度。

因此

$$

\int_{[-1,1]^2} 1_{\{x^2+y^2\le1\}}\,d\mu
=
\frac14
\int_{-1}^1
\int_{-1}^1
1_{\{x^2+y^2\le1\}}
\,dy\,dx
$$

由 Fubini 定理，对固定 $x$ 有

$$
\int_{-1}^1
1_{\{x^2+y^2\le1\}}\,dy
=
2\sqrt{1-x^2}
$$

于是

$$
P(X^2+Y^2\le1)
=
\frac14\int_{-1}^1 2\sqrt{1-x^2}\,dx
=
\frac{\pi}{4}
$$

## Monte Carlo 方法

那么你就会问了，为什么闭眼乱扔就能确保计算是对的？

假设我们要算这样一个积分

$$
I = \int_\mathbb{R} f(x)\, d\mu(x)
$$

其中 $\mu$ 是某有限测度,即

$$
0<\int_\mathbb{R} 1_\mathbb{R} \, d\mu(x) = C <\infty
$$

且该积分绝对收敛，即

$$
I = \int_\mathbb{R} |f(x)|\, d\mu(x) <\infty 
$$

那么这时候定义 
$$
\mu_F = \frac{\mu}{\int_\mathbb{R} 1_\mathbb{R} \, d\mu}
$$

就把原积分化为

$$
I = \int_\mathbb{R} 1_\mathbb{R} \, d\mu \int_\mathbb{R} f(x) \, d\mu_F(x)
$$

这样我们就可以定义分布函数

$$
F(x) = \mu_F((-\infty, x])
$$

这样我们就能定义 $F$ 的左连续逆

$$
F^{-1}(u)
=
\inf\{x\in\mathbb{R} : F(x) \ge u\}.
$$

然后我们从 $((0,1), \mathcal{B}(0, 1), \lambda)$ 中得到一个服从均匀分布的随机变量 $
U \sim U(0,1)
$

这样我们定义

$$
X = F^{-1} \circ U
$$

可以证明 $P(X\le x) = F(x)$

所以对于 **任意分布函数F必存在一个概率空间( $\Omega$ , $\mathcal{F}$ , P)和它上面的随机变量使得 $X \sim F$**

这样利用测度变换我们就把原积分化为了

$$I = \int_\mathbb{R} 1_\mathbb{R} \, d\mu \int_\Omega f(X) \, dP$$

这样从$F$中采样独立同分布的

$$
X_i \sim \mu_F,\quad, i \in [1, N] \cap \mathbb{N}
$$

然后定义估计量

$$
\hat I_N
=
\frac1N \sum_{i=1}^N f(X_i)
$$

根据强大数定律(Strong Law of Large Numbers, SLLN)，由于 

$$ \mathbb{E}_P (|f(X_i)|) = \int_\Omega |f(X_i)| \, dP <\infty $$

所以有

$$
\hat I_N
\to
\int f\, d\mu_F,\quad a.s.,
\qquad (N\to\infty)
$$

这样的话我们就得到了

$$
I \approx \frac1N \sum_{i=1}^N f(X_i) \int_\mathbb{R} 1_\mathbb{R} \, d\mu 
$$

这就是 Monte Carlo 方法的基本原理。

## 重要性采样 (Importance Sampling)

设 $(\Omega,\mathcal F,P)$ 为概率空间，随机变量  $X:\Omega\to\mathbb R$


的分布测度(pushforward measure)定义为

$$
\mu = P\circ X^{-1}
$$

我们希望计算积分

$$
I=\int_{\mathbb R} f(x)\,d\mu(x)
$$

在很多情况下，直接从 $\mu$ 采样并不容易，因此我们选取另一个更容易采样的概率测度 $\nu$（定义在同一可测空间上），并假设

$$
\mu \ll \nu
$$

也就是当 $\nu(A) = 0$ 时 一定有 $\mu (A) = 0$。
根据 Radon-Nikodym 定理，存在函数

$$
w(x)=\frac{d\mu}{d\nu}
$$

使得

$$
\mu (A) = \int_A w \, d\nu
$$

此时原积分化为

$$
I
=
\int_{\mathbb R} f(x)\,d\mu(x)
=
\int_{\mathbb R} f(x)\,w(x)\,d\nu(x)
$$

如果

$$
X_1,\dots,X_N \sim \nu,
$$

则 Monte Carlo 估计量为

$$
\hat I_N
=
\frac1N
\sum_{i=1}^N
f(X_i)w(X_i).
$$

在常见情形下，若 $\mu,\nu$ 是连续型随机变量的分布测度，也就是都绝对连续于 Lebesgue 测度 $\lambda$ ， 则存在概率密度函数

$$
p(x)=\frac{d\mu}{d\lambda},\qquad
q(x)=\frac{d\nu}{d\lambda}
$$


那么我们得到

$$
\frac{d\mu}{d\nu}=\frac{p}{q},
\qquad \nu\text{-a.s.}
$$

因此

$$
I
=
\int_{\mathbb R}
f(x)\frac{p(x)}{q(x)}\,d\nu(x)
=
\int_{\mathbb R}
f(x)\frac{p(x)}{q(x)}q(x)\,d\lambda(x)
$$

于是 importance sampling 的 Monte Carlo 估计量写成

$$
\hat I_N
=
\frac1N
\sum_{i=1}^N
f(X_i)\frac{p(X_i)}{q(X_i)}
$$

## 好了你已经学会了Monte Carlo，不妨来试试吧！
好了，相信你已经学会了怎么用蒙特卡罗方法来算积分，不妨来用下面这道题来检验一下自己吧！

$$
I=\int_0^\infty \frac{e^{-x}}{1+x^2}\,dx
$$

**小贴士**
注意到积分区间是 $[0,\infty)$，因此直接从均匀分布里采样并不现实。注意到

$$
\int_0^\infty e^{-x}\,dx = 1
$$

想想看！

---

> 哦什么？
> 
> 你还有个问题，
>
> 什么是测度？  
>  
> emm...  
> 测度就是，  
>  
> 先这样这样，  
> 再那样那样，  
> 以后再说吧！