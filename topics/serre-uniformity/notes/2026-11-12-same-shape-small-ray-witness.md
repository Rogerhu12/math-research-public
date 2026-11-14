# 同形单素数判别式下，R56 的第一条射线关系确可成立

**状态：已证明的小例边界；不是 R53 的 387 位实例判定。**

取
$$
n=52632=2^3 3^2\cdot17\cdot43,\qquad
q=432n^2-1=1196695047167,
$$
$$
L=\mathbb Q(\theta),\qquad \theta^3-\theta-8n=0.
$$
素数 $q$ 的穷尽试除、模 $13$ 不可约性和下述证书，由同目录
`verify_r56_same_shape_ray_witness.py` 用 Python 标准库验证，运行约一秒：

```bash
python -B topics/serre-uniformity/notes/verify_r56_same_shape_ray_witness.py
```

令 $\beta=(\theta^2+\theta)/2$。乘法式
$$
\theta^2=2\beta-\theta,\qquad
\theta\beta=\beta+4n,\qquad
\beta^2=\beta+2n\theta+4n
$$
证明 $\mathbb Z[1,\theta,\beta]$ 为整环中的秩三阶，其判别式为素数 $-q$，故已经最大。$2$ 完全分裂，仍记
$$
\mathfrak p_0=(2,\theta,\beta),\qquad
c_0=[\mathfrak p_0]\in\operatorname{Cl}_{(3)}(L).
$$
此例满足 $v_2(n)=3$、$3\cdot43\mid n$、$q\equiv-1\pmod{172}$，而且
$$
\boxed{14c_0=0,\qquad\text{因而 }42c_0=0.}
$$

## 压缩证书的内容和证明

验证器的常量 `ROWS` 有 $39$ 行 $(a_j,b_j,e_j,f_j)$，完整定义两个显式元素
$$
\alpha=\prod_j(a_j+b_j\theta)^{e_j},\qquad
\varepsilon=\prod_j(a_j+b_j\theta)^{f_j}.
$$
负指数按域中逆元解释，不须存储展开后的巨大整数。证书直接证明
$$
(\alpha)=\mathfrak p_0^{14},\quad N\alpha=2^{14},
\qquad (\varepsilon)=\mathcal O_L,\quad N\varepsilon=1.
$$
这些断言不使用 PARI 的类群计算正确性、GRH 或“基本单位”假设。

具体地，每个因子的范数是
$$
N(a+b\theta)=a^3-ab^2+8nb^3.
$$
所有非有理因子均有 $(a,b)=1$。其范数的全部素因子不超过 $103$，因此全可直接试除。对奇素数 $\ell$，这些范数不被 $q$ 整除，$\ell$ 不分歧；若 $\ell\mid N(a+b\theta)$，唯一可能的素理想是 $\theta\equiv-a/b\pmod\ell$ 的一次素理想，其赋值正是 $v_\ell(N(a+b\theta))$。有理因子所涉的 $3,17,29,43,101$ 均完全分裂，逐个根检查。

$2$ 处分别提升 $\theta_0\equiv0\pmod2$、$\theta_+\equiv1\pmod4$、$\theta_-\equiv-1\pmod4$。后两者写为 $\pm1+4t$，对应简单根方程
$$
t\pm6t^2+8t^3-n=0.
$$
模 $2^{16}$ 已超过每个因子所需精度。验证器将全部 $33$ 个相关素理想的赋值逐项相加，结果分别只有 $\mathfrak p_0^{14}$ 和空除子。这同时证明 $\alpha$ 整、$\varepsilon$ 为单位。

$3$ 处分别提升 $\theta\equiv0,1,-1$ 的三个简单根。每个因子先除去其准确的 $3$ 次幂，再计算剩余单位；不能对含 $3$ 分母的压缩乘积直接模 $3$ 相除。总赋值在三处全为零，结果为
$$
\alpha\equiv\varepsilon\equiv(2,1,2)
\quad\text{于 }\mathcal O_L/(3)\simeq\mathbb F_3^3.
$$
故 $\gamma=\alpha\varepsilon$ 满足
$$
(\gamma)=\mathfrak p_0^{14},\qquad \gamma\equiv1\pmod{3\mathcal O_L},
$$
这就是所需射线关系。证书只证明阶整除 $14$；未声称其准确阶为 $14$。

## 范围

此例补上此前反检验未包含的“同一特殊多项式、单素数最大判别式及 $2,3,43$ 条件”。这些条件不能单独保证 R56 的三条关系全部失败。它没有 R53 的全部小素数分裂窗口，也未证明
$$
u(u+v)(2u+v)-2nv^3=\pm2q^{21},\qquad (u,v)=1,\quad3\mid v
$$
有原始全局解。即使上述射线关系成立，缺失坐标为零的单位轨道问题仍保留；R53 原来的 $n$、$q$ 和三条指定关系也仍未判定。
