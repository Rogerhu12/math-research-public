# R835 — 互素 CM 导子迫使一个原混合伴随因子为奇符号

日期：2026-11-15。**状态：下列符号障碍及其三重积推论已证明。**

本篇固定原 $\lambda_\ell$，只审计一种具体修复：
将低权第一 CM 因子改成导子与共轭互素的角色，以尝试使用临界 Hecke 的单位作用。
结论是这种修改必定引入另一个中心零，不能同时保留 R826 的简单复零和
R832 所用的三个混合中心值非零。本篇不否定其他临界比较，也不证明任何新的 AJ 非零。

## 1. 固定数据和结论

令 $K=\mathbf Q(\omega)$，$c$ 为复共轭，$\mathrm N$ 为范数 Hecke 角色。
固定 R806/R818/R826 的任意一条
$$
\lambda=\lambda_\ell=\eta_\ell^{-1}\psi_0^3,\qquad
\ell\in\{4,10,16\}.
\tag{1}
$$
它的无穷型为 $(3,0)$，准确有限导子为 $(34\delta)$，
其中 $\delta$ 生成 $K$ 中位于 $3$ 上方的素理想。原完整角色满足
$$
\lambda\lambda^c=\mathrm N^3,\qquad
\lambda|_{\mathbf A_{\mathbf Q}^{\times}}
=\mathrm N^{3/2}|_{\mathbf A_{\mathbf Q}^{\times}}\epsilon_{K/\mathbf Q}
\tag{2}
$$
的单位化版本；等价地，$AI(\lambda)$ 的权四形式具有平凡 nebentypus。
这里写出的第二式按 idelic 范数使用；其内容是
$\lambda^{\rm u}|_{\mathbf A_{\mathbf Q}^{\times}}=\epsilon_{K/\mathbf Q}$，
$\lambda^{\rm u}:=\lambda\mathrm N^{-3/2}$。

[R826(13)](R826-fixed-low-weight-cm-triple-and-fourth-de-rham-slot.md)
给原 $K$-Hecke 单位化 epsilon 值
$$
(W_2(\lambda^{\rm u}),W_3(\lambda^{\rm u}),
 W_{17}(\lambda^{\rm u}),W_\infty(\lambda^{\rm u}))
=(1,-i,1,-i).
\tag{3}
$$
其余有限地方未分歧，值为 $1$。
[R818](R818-original-three-weight-four-complex-analytic-rank-one.md)
另已证明 $\operatorname{ord}_{s=2}L(\lambda,s)=1$。

取任意固定代数 Hecke 角色 $\psi_a$，无穷型 $(1,0)$，准确有限导子
$\mathfrak c$ 满足
$$
\mathfrak c+\mathfrak c^c=\mathcal O_K.
\tag{4}
$$
定义实际反循环角色及混合伴随角色
$$
a=\psi_a/\psi_a^c,\qquad
\gamma_a=\frac{\lambda}{\mathrm N a}.
\tag{5}
$$
则 $\gamma_a$ 的无穷型为 $(1,0)$，满足
$\gamma_a\gamma_a^c=\mathrm N$，
而且 $AI(\gamma_a)$ 为平凡 nebentypus 的权二 CM 形式。
准确有限导子为
$$
\mathfrak f(\gamma_a)=(34\delta)\mathfrak c\mathfrak c^c.
\tag{6}
$$
要证的结论是
$$
\boxed{W(\gamma_a)=-1,\qquad L(\gamma_a,1)=0.}
\tag{7}
$$
这里不要求 $\psi_a$ 本身具有平凡 nebentypus。

## 2. 原三个有限地方不改变

由 (4)，$\mathfrak c$ 不能含任何自共轭素理想，
也不能同时含一对共轭的不同素理想。
所以它只支撑于分裂有理素数的一侧。
$2,17$ 在 $K$ 中惰性，而 $3$ 分歧；故
$$
(\mathfrak c,34\delta)=1.
\tag{8}
$$

在任何自共轭素理想 $\mathfrak q$，$\psi_a$ 未分歧。
共轭保持其赋值，故 $\psi_a$ 和 $\psi_a^c$ 的两个未分歧局部角色相等：
不只单位上的限制相等，均匀化元上的值也相等。因此
$$
a_{\mathfrak q}=1.
\tag{9}
$$
$\gamma_a^{\rm u}:=\gamma_a\mathrm N^{-1/2}
=\lambda^{\rm u}a^{-1}$。
由 (9)，在 $2,3,17$ 的全部局部角色均与 $\lambda^{\rm u}$ 相同；
(3) 中原有限乘积仍准确为 $-i$。

由定义 $a$ 在 $\mathbf A_{\mathbf Q}^{\times}$ 上恒为 $1$。
因此 $\gamma_a^{\rm u}$ 在该群上的限制仍为 $\epsilon_{K/\mathbf Q}$；
这证明了 (5) 后的平凡 nebentypus 断言。
在新的分裂素数的每一侧，$\lambda^{\rm u}$ 都未分歧，
而 $\psi_a/\psi_a^c$ 的 ramified 部分仅来自该侧的原 $\psi_a$ 或其逆；
没有可消去的另一 ramified 因子。这同时证明 (6)。

## 3. 每个新增分裂素数的准确符号

设 $q$ 是 $\mathfrak c$ 支撑下方的有理素数，选
$\mathfrak q\mid\mathfrak c$，则 $\mathfrak q^c\nmid\mathfrak c$。
由于 $q$ 分裂，
$K_{\mathfrak q}\simeq K_{\mathfrak q^c}\simeq\mathbf Q_q$。
$\gamma_a^{\rm u}$ 在这两个地方的角色互为逆：
其乘积是限制到 $\mathbf Q_q^\times$ 的角色，而
$\epsilon_{K/\mathbf Q,q}=1$。写这一对为
$$
\xi_q,\quad \xi_q^{-1},\qquad
\xi_q|_{\mathbf Z_q^\times}
=\psi_{a,\mathfrak q}^{-1}|_{\mathbf Z_q^\times}.
\tag{10}
$$

两处使用由同一全局 trace 加性角色诱导的标准加性角色。
局部 Gauss 和反射恒等式给
$$
W(\xi_q)W(\xi_q^{-1})=\xi_q(-1)
=\psi_{a,\mathfrak q}(-1).
\tag{11}
$$
为明确规范，若 $\chi$ 是模 $q^n$ 的 primitive 单位角色，
则其有限和满足
$\tau(\chi)\tau(\chi^{-1})=\chi(-1)q^n$。
两个 $q^{-n/2}$ 消去 $q^n$；任意未分歧均匀化元因子在互逆两项中抵消。
这便是 (11)，包括非平凡未分歧 twist，没有省略额外相位。
逆在 $-1$ 上不改变值，因为该值属于 $\{\pm1\}$。

注意 (11) 是同一个分裂有理素数上两个 $K$-局部 epsilon 的乘积。
本篇没有在 (3) 的 $K$-Hecke 规范中另插入一个 $AI$ induction constant；
全部地方的全局 induction constants 乘积为 $1$。

## 4. 所有新增符号的乘积被全局单位固定

把全局主 idèle $-1$ 代入 $\psi_a$。
无穷型 $(1,0)$ 的无穷分量在 $-1$ 上为 $-1$；
所有未分歧有限分量在单位 $-1$ 上为 $1$。
由 (4) 的单侧支撑，余下的全部有限分量正好是 (11) 里的那些项。
全局角色在主 idèle 上恒为 $1$，因而
$$
\boxed{
\prod_{q\mid\mathrm N\mathfrak c}\psi_{a,\mathfrak q}(-1)=-1.
}
\tag{12}
$$
所以不能将各新增分裂处都任意选成 $+1$。
这也说明无穷型 $(1,0)$ 的角色不可能在此条件下具有空有限导子。

$\gamma_a$ 的型差为 $1$，故在 (3) 的同一复地方规范中
$W_\infty(\gamma_a^{\rm u})=i$。
合并原有限值、新增分裂值和无穷值，得到
$$
W(\gamma_a)=(-i)\,(-1)\,i=-1.
\tag{13}
$$
$AI(\gamma_a)$ 自对偶且中心在 $s=1$，
其 primitive $L$ 函数是整函数；(13) 的函数方程立即给 (7)。
证明不依赖目标 $p$，也没有使用数值扫描。

## 5. 对任何同原最高因子的低权三重积的推论

进一步取无穷型均为 $(1,0)$ 的角色 $\psi_b,\psi_c$，使
$$
\psi_a\psi_b\psi_c=\lambda.
\tag{14}
$$
这里只要求第一角色满足 (4)。
在三个二维诱导的张量中，全未共轭行与其共轭给 $AI(\lambda)$；
仅共轭第一输入的行及其共轭给
$$
\psi_a^c\psi_b\psi_c=\lambda/a=\mathrm N\gamma_a.
\tag{15}
$$
因此准确 primitive 分解含有
$$
L(AI(\psi_a)\otimes AI(\psi_b)\otimes AI(\psi_c),s)
=L(\lambda,s)L(\gamma_a,s-1)L(\gamma_b,s-1)L(\gamma_c,s-1),
\tag{16}
$$
其中 $\gamma_b=\lambda/(\mathrm N(\psi_b/\psi_b^c))$、
$\gamma_c=\lambda/(\mathrm N(\psi_c/\psi_c^c))$。
每个混合角色的无穷型是 $(1,0)$；故它们都非共轭不变，
其二维 CM $L$ 函数均整，不存在抵消中心零的极点。
完整局部角色的张量分解保证 (16) 包含全部坏 Euler 因子，
不用 imprimitive 删除作掩饰。

由 R818 和 (7)，得到
$$
\boxed{
\operatorname{ord}_{s=2}
 L(AI(\psi_a)\otimes AI(\psi_b)\otimes AI(\psi_c),s)\ge2.
}
\tag{17}
$$
特别不能在 (4)、(14) 下保持 R826 的原解析秩一，
也不能保持 R832 使用的“三个混合 $L(1)$ 全非零”前提。
(17) 本身没有断言新混合 Mordell–Weil 秩为正或某个新对角类为零。

## 6. 临界 Hecke 定理的使用范围

Castella–Wang-Erickson 的
[《Critical Lambda-adic modular forms and bi-ordinary complexes》](https://web.math.ucsb.edu/~castella/CG2.pdf)
Theorem 8.2.6 将有关单位模与一个 degree $-1$ Hecke 作用相认，
并明确采用 [CWE22, §1.2.3] 的条件。
其 [《Class groups and local indecomposability for non-CM forms》](https://web.math.ucsb.edu/~castella/Greenberg.pdf)
§1.2.3(4) 正是残余诱导角色的 prime-to-$p$ 导子
$\mathfrak c+\mathfrak c^c=\mathcal O_K$。
这里两份原文的相应段落已核，不省该条件。

对一条先于目标 $p$ 固定的代数角色，在排除其导子和有限 inertia 像阶的素因子后，
有限 inertia 角色的模 $p$ 约化保持导子。因此上述条件与 (4) 一致，
适用于当前“换一个固定辅助因子，再变动目标 $p$”的尝试。
原 $\psi_{17}$ 的导子为 $34\delta$，在 $2,3,17$ 都含自共轭素理想；
原另两低权角色的导子为 $17\delta$，也不满足此互素条件。

本篇证明：若只用满足 (4) 的固定新第一因子解决这个假设，同时保持原最高角色
$\lambda_\ell$，就必须面对 (7)、(17) 的新混合中心零。
即使今后有适用于原导子的扩展定理，仍须把原
$\pi_f[\Xi_{02}]$ 的完整两项杯积与指定 canonical $\lambda_\ell$ 类比较；
形式上的 Hecke 作用或反循环角色乘法恒等式均没有单独完成该步骤。
