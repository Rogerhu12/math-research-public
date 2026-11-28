# R1211：原最高惯性角色全部 deck 部分的尖点投影整性

日期：2026-11-28。会话：Astra-serre-24b8836b-20261126；root / global_route。

**已证明。** R1202 对最高惯性权、负 deck 的整性可以扩展到同一最高惯性角色的全部 deck 部分。新增的唯一中心可能项是第 $1$ normal 的 $db/u$；它沿真实 SS 节点在第 $m$ normal 产生一个明确非零极部，仍被已有完整尾消去排除。本篇不把这个角色格结论改称原整个 Hodge 格或整个 $p$-divisible 群的整分裂。

## 1. 量词与原对象

保持 R1202 的
$$
p=12g-1>37,\quad m=(p-1)/2,\quad
e_0=m(p+1),\quad R=W[\pi_0],\quad\pi_0^{e_0}=p,
$$
$$
\Lambda=H^0(\mathscr X,\omega_{\mathscr X/R}),\quad
E=E_m,\quad U=U_m=p\,e_{V_m}e_N,\quad q=U/p.
\tag{1211.1}
$$
它们来自同一个 full-$p$ 曲线、原六标记及实际正规化子对应；全部非零 Weil 配对分支保留。原关系为
$E^2=E$、$EU=UE=U$、$U^2=pU$。

现在仅要求一个给定实际整微分满足
$$
\Omega\in E\Lambda,\qquad
\sigma^*\Omega=\xi^{m^2}\Omega,
\tag{1211.2}
$$
不再限制它的 $\delta^*$ 角色。结论是
$$
\boxed{\quad U\Omega\in p\Lambda,\qquad q\Omega\in E\Lambda.\quad}
\tag{1211.3}
$$
因此这也同时适用于两个非平凡 deck 角色以及旧 deck 部分；没有把其中任一部分的维数或特殊底映射强行认作负 deck 的对应对象。

## 2. 已付完整尾消去没有使用 deck 假设

R1202 §§2–4 已证明同一个实际 $\overline U$ 在所有
$$
M_N=\operatorname{Sym}^{(N+1)(p-1)-2}(k^2)
       \otimes\det^{1-m},\qquad 0\le N\le p,
$$
上为零。两个临界 $N=p-1,p$ 使用真实极化 jet 映射及直和，未靠组成因子个数作结论。该群模恒等式与曲线 deck 角色无关。

对 (1211.2)，中心特殊纤维仍为零：其角色均为 $p+1$ 的倍数，而 $m^2\equiv1\pmod{p+1}$。所以任意中心 incoming 项的 normal 阶至少为一。原厚度一 generic 节点、厚度三 CM 节点、全部 normal–pole 界和完整 framing determinant 运输仍逐字适用。它们把每个 $n<e_0$ 的实际尾系数放入上述同一 $M_N$。

于是已有证明给
$$
(U\Omega)|_{\text{所有 positive-genus 尾的仿射开}}
\equiv0\pmod p.
\tag{1211.4}
$$
没有重新扫描任何 normal 窗口，也不将这个仿射结论直接当作全局可除 $p$。

## 3. 全部剩余中心可能项

若 (1211.3) 不成立，沿原自由 Hodge 格取最小全局阶
$$
U\Omega=\pi_0^h\Omega',\qquad
0\le h<e_0,\quad \bar\Omega'\ne0.
$$
由 (1211.4) 及原 compact-type 树，$\bar\Omega'$ 必是一条非零中心全纯微分。原 $E$ 的特殊晶体权只有
$$
\pm m^2,\quad\pm(m^2-1)\pmod{e_0}.
$$
中心权须为 $p+1$ 的倍数，故仍只可能是以下两种：

| 中心角色 | 首全局阶 $h$ | 整个中心全纯空间 |
|---|---:|---|
| $m^2-1$ | $1$ | $k\,db/u$ |
| $(m+1)^2$ | $e_0-p$ | $uT(b)db/(rA)$，$\deg T\le m-2$ |

第二行与 R1202 §5 完全相同。若 $T(s)\ne0$，原 SS 节点在 normal $h+1=e_0-p+1<e_0$ 产生非零二阶极部；较高中心层不能抵消最高 pole。故所有 $m-1$ 个简单 SS 根均须使 $T$ 为零，与 $\deg T\le m-2$ 矛盾。这个论证本来就只用了整个次数界，不需要负 deck 条件。

只需处理第一行。R1202 原先用负 deck 将它排除；下面用其实际节点项支付全部 deck 情形。

## 4. 新增 $db/u$ 项在原 SS 节点的非零 pole

若 $h=1$，写 $\bar\Omega'=c\,db/u$，$c\in k^\times$。在任意原 SS 点 $s$，保留真实节点单位
$$
b-s=\kappa_s w_s^m+\cdots,\qquad
u=\lambda_s w_s+\cdots,\qquad
z_sw_s=\rho_s\pi_0,
$$
其中 $m,\kappa_s,\lambda_s,\rho_s$ 全为单位。中心首项准确为
$$
\pi_0c\frac{db}{u}
=\pi_0\frac{cm\kappa_s}{\lambda_s}
w_s^{m-2}\,dw_s+\cdots.
\tag{1211.5}
$$
将同一节点关系代入，尾上第 $m$ normal 的最高极部为
$$
\boxed{\quad
-\frac{cm\kappa_s\rho_s^{m-1}}{\lambda_s}
\,\pi_0^m z_s^{-m}\,dz_s.
\quad}
\tag{1211.6}
$$
它非零，且 $m<e_0$。若一个更高中心层的全局阶是 $h'>1$，它在同一 normal $m$ 的 pole 至多 $m-h'+1<m$。同一首中心层的更高 Taylor 项进入更高 normal；真实节点单位的重参数保持这个 normal–pole 滤过。因此 (1211.6) 的最高项不能由任何这些项抵消。

这与 (1211.4) 在原尾仿射开上的整个模 $p$ 消失矛盾。第一行也被排除，证明 (1211.3)。有理链按同一 dualizing sheaf 合同；没有另一个可取消该 pole 的链上全纯项。

## 5. 所得准确整格与继续范围

记整个最高惯性角色的 $W$-格为
$$
\Gamma_{\rm all}=\{\Omega\in E\Lambda:
                 \sigma^*\Omega=\xi^{m^2}\Omega\}.
$$
由 (1211.3) 和原对应的交换性，
$$
\boxed{\quad
\Gamma_{\rm all}=q\Gamma_{\rm all}
                  \oplus(1-q)\Gamma_{\rm all}.
\quad}
\tag{1211.7}
$$
原 $\delta$ 的阶为三，是单位，所以各 deck 部分也分别整分裂。负 deck 部分正是 R1202–1205 的原 $\Gamma$，其秩与 Cartier 核识别保持原结论。

正 deck 中确有中心 $\pi_0db/u$ 这一允许的最高角色方向；本篇消去的是它作为 $U\Omega$ 在除 $p$ 前的首层，而没有把它从一般 $\Omega$ 或 $q\Omega$ 的实际格中删除。因此不能把正 deck 的 generic 底映射自动称为单射，也不能照搬负 deck 的 $\ker\mathfrak c$ 维数公式。

(1211.7) 是特定惯性角色格的整幂等分裂，不声称 $q$ 已保持整个 $R$-Hodge 格。实际最高型的协变晶体、极化 $B=\langle F\alpha^{-1}(-),-\rangle$、Hodge graph 及 whole-MW 法向比较仍须在同一个原模型上另付。

## 来源与核验

- R1202 §§2–4：全部 polynomial normal 模、临界 jet、完整分支与 tail affine 模 $p$ 消去；§5：中心两种全纯角色及高 PS 极部论证。
- R1028、R1193：同一 $u^m=r^{n+1}A$、真实 SS/CM 节点及所有单位。
- R1204–1205：负 deck 中的实际返回、纯尖点整基及底读取范围。

root 与 global_route 独立纸核新增 $h=1$ 分支的 normal、pole、系数和高层不能抵消的界。未执行数学程序，未重做已登记窗口。Serre 主目标仍 OPEN。
