# R218：慢 dyadic 符号的精确径向半群型和预解型

日期：2026-11-13（UTC+8）。作者：normal_states。

状态：全部渐近式及量词有完整证明。本文把同轮的阶与正有限型推进为每个方向相同的精确型，仍不解决普通不变子空间、正常湮灭态或任意未知限制的稠密像。

## 1. 陈述与统一常数

逐位任取 $X_j\in\{N_j,Y_j\}$，其中
$$
N_j=A^{2^j}/d_j,\qquad Y_j=N_j(I+N_j)^{-1}.
$$
取任意复系数，只有模长要求
$$
|c_j|=(j+1)^{-2},\qquad T=\sum_{j\ge0}c_jX_j.
\tag{1.1}
$$
所有相位均可任意，$N/Y$ 的选择亦无一致性要求。

置绝对常数
$$
\mathsf C=\int_0^\infty\operatorname{arsinh}\!\left(\frac1{2x^2}\right)dx
=\frac{\Gamma(1/4)^2}{2\sqrt{2\pi}}
=2.622057554292119810\ldots,
$$
$$
\mathsf K=\frac{\mathsf C^2}{4}
=\frac{\Gamma(1/4)^4}{32\pi}
=1.718796454505093207\ldots.
\tag{1.2}
$$
小数仅用于识别常数，不参加证明。

**定理1.1。** 对 (1.1) 的整个算子族，以下大 $O$ 常数为绝对常数，特别不依赖全部系数相位、逐位 $N/Y$ 选择及复方向：
$$
\boxed{
\log\|e^{zT}\|
=\mathsf C\sqrt{|z|}+O\!\bigl(\log^2(|z|+2)\bigr)
\quad(|z|\to\infty).
}
\tag{1.3}
$$
以及
$$
\boxed{
\log\!\left(|\lambda|\,\|(\lambda I-T)^{-1}\|\right)
=\frac{\mathsf K}{|\lambda|}
+O\!\left(\log^2\left(2+|\lambda|^{-1}\right)\right)
\quad(\lambda\to0,\ \lambda\ne0).
}
\tag{1.4}
$$
因此 $z\mapsto e^{zT}$ 的阶准确为 $1/2$，每个方向的型准确为 $\mathsf C$；$w\mapsto(I-wT)^{-1}$ 的阶准确为1，每个方向的型准确为 $\mathsf K$。这里说的是全空间算子范数，没有把它当成各向量或各不变子商的局部增长结论。

## 2. 从同轮实际证明继承的输入

使用同轮两篇完整证明稿：

- [R215](R215-slow-semigroup-resolvent-and-normal-annihilator-tail.md)；
- [R217](R217-slow-symbol-entire-order-and-directional-resolvent-growth.md)。

所需输入只有以下逐项已证的真实算子估计：
$$
N_j=E_j+\eta_jE_j^*N_{j+1},\quad
N_j^2=\eta_jN_{j+1},\quad
0<\eta_j\le e^{-77016^j},
\tag{2.1}
$$
以及对有限头、纯尾混合的同一版本
$$
\|X_j\|\le3,\qquad
\|X_j^n\|\le3^n e^{-16^j n^4}\quad(n\ge2).
\tag{2.2}
$$
相应单因子上界为
$$
\log\|e^{wX_j}\|
\le \log 2+\log(1+3|w|)
+16^{-j/3}\bigl(\log_+(3|w|)\bigr)^{4/3}.
\tag{2.3}
$$
全部慢和及下述混合模型都满足
$$
\|e^{zT}\|\le e^{16\sqrt{|z|}},\qquad
\|(\lambda I-T)^{-1}\|
\le2|\lambda|^{-1}e^{128/|\lambda|}.
\tag{2.4}
$$
第二个式子包括全部复 $\lambda\ne0$，由旋转后范数 Laplace 积分给出真实左右逆，特别谱为 $\{0\}$。

记有限头截断为 $X_j^{[k]}$，置
$$
H_k=\sum_{j<k}c_jX_j^{[k]},\qquad
D_k=\sum_{j\ge k}c_jE_j,\qquad
\widehat T_k=H_k+D_k.
\tag{2.5}
$$
低头保留全部实际 carry，只在第 $k$ 位切断；纯尾与低头作用于不同张量因子。
已经逐项支付的实际差为
$$
\|T-\widehat T_k\|\le26\eta_{k-1}.
\tag{2.6}
$$
在 R174 的等距孔表示中，低头 $H_k$ 杀掉低头真空。该表示只用于算子范数和指定向量测试；不将其向量认作 Haar 向量。

## 3. 纯尾半群范数的精确乘积

单个二维消灭矩阵 $E$ 满足 $E^2=0$。直接计算 $I+wE$ 的最大奇异值得
$$
\|I+wE\|=\frac{\sqrt{4+|w|^2}+|w|}{2}
=\exp\bigl(\operatorname{arsinh}(|w|/2)\bigr).
\tag{3.1}
$$
对有限个不同位，Hilbert 张量积范数精确相乘。无穷和按算子范数收敛，其指数也是有限乘积的范数极限，故
$$
\boxed{
\log\|e^{zD_k}\|
=\sum_{j\ge k}\operatorname{arsinh}\!\left(\frac{|z|}{2(j+1)^2}\right).
}
\tag{3.2}
$$
该式对全部相位准确成立，并非只给范数上界。

记
$$
P(r)=\sum_{n=1}^\infty\operatorname{arsinh}\!\left(\frac r{2n^2}\right).
$$
被积函数正且单调下降，积分比较及变量代换给
$$
P(r)=\int_0^\infty\operatorname{arsinh}\!\left(\frac r{2x^2}\right)dx+O(\log(r+2))
=\mathsf C\sqrt r+O(\log(r+2)).
\tag{3.3}
$$
为明确端点误差，对 $0<x\le1$，
$$
\operatorname{arsinh}(r/(2x^2))
\le\log(1+r/x^2)
\le\log(1+r)+2|\log x|.
$$
其在 $(0,1)$ 的积分至多 $\log(1+r)+2$，而第一项亦为 $O(\log(r+2))$；因此 (3.3) 的比较误差完全受控。

分部积分给
$$
\mathsf C=2\int_0^\infty\frac{dx}{\sqrt{1+4x^4}}
=\sqrt2\int_0^\infty\frac{du}{\sqrt{1+u^4}}
=\frac{\sqrt2}{4}B(1/4,1/4),
$$
即 (1.2)。两个分部积分端点均为0：$x\log(1/x)\to0$ 于0，而 $x\operatorname{arsinh}(1/(2x^2))\to0$ 于无穷。

## 4. 实际低头只改变对数平方量级

给定 $r=|z|\ge16$，取
$$
k=1+\lceil\log_{16}(r+1)\rceil=O(\log(r+2)).
$$
头尾精确张量分解给
$$
\|e^{z\widehat T_k}\|=\|e^{zH_k}\|\,\|e^{zD_k}\|.
\tag{4.1}
$$
有限头 $H_k$ 幂零，所以 $e^{zH_k}$ 有特征值1，故其范数至少1。由 (2.3)、$\sum_j16^{-j/3}<2$，又有
$$
0\le\log\|e^{zH_k}\|
\le k\log(2(1+3r))+2\bigl(\log_+(3r)\bigr)^{4/3}
=O(\log^2(r+2)).
\tag{4.2}
$$
全部有限头项两两交换，故这里可用单因子估计相加。

从 (3.2) 删去前 $k$ 项的成本至多
$$
k\operatorname{arsinh}(r/2)=O(\log^2(r+2)).
\tag{4.3}
$$
因此 (3.3)—(4.3) 给
$$
\log\|e^{z\widehat T_k}\|
=\mathsf C\sqrt r+O(\log^2(r+2)).
\tag{4.4}
$$

最后必须回到实际 carry。由 $\|T\|\le6$、$\|\widehat T_k\|\le8$、Duhamel 恒等式及 (2.6)，
$$
\|e^{zT}-e^{z\widehat T_k}\|
\le26r\exp(8r-770(r+1))\le e^{-700r}.
\tag{4.5}
$$
由于 $\|e^{z\widehat T_k}\|\ge1$，(4.5) 对范数对数的改变量至多 $2e^{-700r}$。从 (4.4) 得 (1.3)。所有估计只依赖 $r$，故全部统一性已经保留。

## 5. 精确半群型给精确预解上型，含误差率

由 (1.3) 及紧参数段上的 (2.4)，有绝对 $B>0$ 使对整个算子族、所有 $t\ge0$ 及全部方向 $\theta$，
$$
\|e^{t e^{-i\theta}T}\|
\le\exp\bigl(\mathsf C\sqrt t+B\log^2(t+2)\bigr).
\tag{5.1}
$$
取 $\lambda=q^{-1}e^{i\theta}$、$q\ge1$。旋转后的真实 Laplace 积分给
$$
\|(\lambda I-T)^{-1}\|
\le\int_0^\infty
\exp\bigl(-t/q+\mathsf C\sqrt t+B\log^2(t+2)\bigr)dt.
\tag{5.2}
$$
令 $\sqrt t=qv$。利用
$$
2+q^2v^2\le(q+2)^2(1+v)^2,\qquad \log(1+v)\le v,
$$
得到
$$
B\log^2(2+q^2v^2)
\le8B\log^2(q+2)+8Bv^2.
$$
所以 (5.2) 至多
$$
2q^2 e^{8B\log^2(q+2)}
\int_0^\infty v\exp\bigl(-(q-8B)v^2+\mathsf Cqv\bigr)dv.
\tag{5.3}
$$
若 $q\ge16B$，配方的最大指数满足
$$
\frac{\mathsf C^2q^2}{4(q-8B)}
\le\mathsf Kq+16\mathsf K B.
$$
配方后的 Gaussian 积分至多为绝对常数乘 $q^{-1/2}$：中心
$\mathsf Cq/(2(q-8B))$ 一致有界，且
$$
\int_{-\infty}^{\infty}|u|e^{-(q-8B)u^2}du=(q-8B)^{-1},
$$
$$
\int_{-\infty}^{\infty}e^{-(q-8B)u^2}du=\sqrt{\pi/(q-8B)}.
$$
因而
$$
\boxed{
\log\!\left(q^{-1}\|(\lambda I-T)^{-1}\|\right)
\le\mathsf Kq+O(\log^2(q+2)).
}
\tag{5.4}
$$
上界没有依赖相位的选择。

## 6. 正锥比较给纯尾预解下界

这是从半群精确型得到相同预解型的关键，不能仅凭一个 Laplace 上界反推。

先在孔表示中把纯尾系数变为正数。若 $\lambda=q^{-1}e^{i\theta}$，对有限孔集 $F$ 的基向量定义 diagonal unitary
$$
Ue_F=\left(\prod_{j\in F}\zeta_j\right)e_F,
\qquad
\zeta_j=e^{i\theta}\overline{c_j}/|c_j|\quad(j\ge k),
$$
并对 $j<k$ 取 $\zeta_j=1$。每个 $F$ 有限，故该式直接定义 $\ell^2$ 上的酉算子，不要求任何无穷相位积收敛。
由于 $E_j$ 消灭一个孔，
$$
U^*(e^{-i\theta}D_k)U=D_k^+,
\qquad D_k^+=\sum_{j\ge k}(j+1)^{-2}E_j.
\tag{6.1}
$$
故纯尾预解范数与 $\theta$ 及所有 $c_j$ 的相位无关。

$D_k^+$ 对孔基的坐标正锥是正算子，其每个幂也为正。对每个 $s>0$、$t\ge0$、整数 $n\ge0$，标量不等式
$$
\frac{t^n}{n!}\le e^{st}s^{-n}
$$
来自 $e^{st}$ 的幂级数。两边乘 $(D_k^+)^n$ 后相加；两列均在范数中收敛，由正锥闭性得到正算子序不等式
$$
0\le e^{tD_k^+}
\le s e^{st}(sI-D_k^+)^{-1}.
\tag{6.2}
$$
这里实际预解的全平面存在已由 (2.4) 保证，且谱半径0保证 Laurent–Neumann 级数对每个 $s>0$ 范数收敛。

对坐标正算子 $0\le R\le Q$，$\ell^2$ 算子范数单调：由 $|Rx|\le R|x|\le Q|x|$ 得 $\|R\|\le\|Q\|$。因此 (6.2) 准确给
$$
\boxed{
\|(sI-D_k^+)^{-1}\|
\ge s^{-1}e^{-st}\|e^{tD_k^+}\|
\quad(s>0,t\ge0).
}
\tag{6.3}
$$
没有在此交换范数与 Laplace 积分，也没有假定某个固定向量同时最大化所有时间的半群范数。

## 7. 保真低头、鞍点尺度与实际预解下型

令 $q=|\lambda|^{-1}\to\infty$，现在取
$$
k=1+\lceil\log_{16}(q+1)\rceil.
$$
注意这里按预解尺度 $q$ 选头，区别于 §4 的半群尺度 $|z|$。在低头真空张量整个尾空间的闭子空间上，$\widehat T_k$ 精确限制为 $D_k$。因此其实际预解同样限制为 $(\lambda I-D_k)^{-1}$，从而
$$
\|(\lambda I-\widehat T_k)^{-1}\|
\ge\|(\lambda I-D_k)^{-1}\|
=\|(q^{-1}I-D_k^+)^{-1}\|.
\tag{7.1}
$$
最后一步使用 (6.1)，单位复标量不改变范数。

在 (6.3) 中取
$$
s=q^{-1},\qquad t=\frac{\mathsf C^2q^2}{4}.
$$
由 (3.2)—(3.3) 及 $k=O(\log q)$，
$$
\log\|e^{tD_k^+}\|
=\mathsf C\sqrt t+O(\log^2(q+2))
=\frac{\mathsf C^2q}{2}+O(\log^2(q+2)).
$$
因此
$$
\log\!\left(q^{-1}\|(\lambda I-\widehat T_k)^{-1}\|\right)
\ge\mathsf Kq-O(\log^2(q+2)).
\tag{7.2}
$$

回到实际 $T$：由 (2.4)、(2.6) 及逆差恒等式，
$$
\|(\lambda I-T)^{-1}-(\lambda I-\widehat T_k)^{-1}\|
\le104q^2 e^{-514q-770}<1
\tag{7.3}
$$
对所有充分大 $q$ 成立。由 (7.2)，模型预解下界指数增长，故减去 (7.3) 的误差最多再损失常数 $\log2$。这给 (1.4) 的下界，结合 (5.4) 完成证明。

## 8. 精确结论与剩余问题

由 (1.3)—(1.4)，一致于 $\theta$ 和 (1.1) 的全部选择，
$$
\frac{\log\|e^{r e^{i\theta}T}\|}{\sqrt r}\longrightarrow\mathsf C,
$$
$$
r\log\!\left(r\|(r e^{i\theta}I-T)^{-1}\|\right)\longrightarrow\mathsf K.
$$
所以此前只知道的正有限型区间现在收缩为指定 Gamma 常数，且全空间范数在首要指数尺度上的方向依赖消失。真实进位只进入已付清的低阶误差，未被预先忽略。

这仍不推出慢符号在所有 Haar 不变子商上具有同样的增长：精确乘积、正锥和低头真空都用于 UHF 全空间的等距孔表示。未知 Haar 子空间没有这些向量的有界交织，不能把全空间下界移植过去。有限秩 Haar-normal 湮灭态仍未排除，普通 Hilbert ISP 的完成标准仍未达到。
