# R97. 三次邻点迹的单位首层正是已知非中央 Stokes 数据

## 准确比较

对全部目标惰性 \(p\ge7\)，实际完整邻点域迹满足
\[
12\operatorname{Tr}\frac{I(r)}{L(r)^3}
\equiv C_4=\beta_4^2\equiv\mathcal S_4^2\equiv1\pmod p.
\]
这里 \(\mathcal S_4\) 是 R62 中已经证明为单位的非中央 Stokes 分支，
目标仍是另一分支 \(\mathcal S_0=-J_{A,p}'(0)\)。

证明使用 R89 的完整尾界及两个边界项
\[
\overline{\varpi^{-3}I(\varpi X)}
=\frac{X^3}{3}+\frac{\kappa_pX^{p+4}}4.
\]
在实际 \(K\) 根上 \(X^{p+1}=-\kappa_p^{-1}\)，两项之差才给 \(1/12\)。
Stokes 变换的全部正层系数有一个 \(p\)，故
\(\mathcal S_4\equiv\beta_4=1\)。
本结果只比较模 \(p\)；没有证明更高精度或特征零恒等式。

## 固定候选机制的准确范围

权 \(m\) 的原全权 Hecke 数据的相对 tame 特征为
\[
\omega_2^{(1-p)m}.
\]
因此 \(m\equiv4\pmod{p+1}\) 的关联数据有阶 \((p+1)/4>1\)，
与基层中心的平凡 tame 分支不同。

固定 \(K=\mathbb Q(i)\)-CM 椭圆扭曲在其导子之外未分歧；
固定素于 \(p\) 的同源、标签及等变 Hecke 箭头保持关联惯性角色。
这些直接等变比较不能将上述非平凡分量同构为基层中央分量。
这是对关联字符数据的陈述，没有把半因子或 Stokes 数值
未经构造便当成 Galois 特征向量。

所以 R89 的单位首层尚未提供固定有限条秩二曲线中心导数的非零组合。
本结果不排除新的标量周期恒等式、非线性比较、
其他 CM 域或非 CM 曲线的独立路线。

## 证明

[全文](../notes/2026-11-12-cubic-neighbor-trace-and-noncentral-stokes.md)
已根端独审，角色断言及其对数值恒等式的限制已逐句澄清。
