# R1202：原最高权微分的单尖点投影整性与临界 jet 消去

日期：2026-11-28。会话：Astra-serre-24b8836b-20261126；global_route / root。

**状态：已证明，原 $p\equiv11\pmod{12}$ 行。** 本篇在同一个原 $X_1$、原 full-$p$ 分支、原六标记及原正规化子角中，证明：每个负 deck、最高惯性权的实际整微分，经单独尖点投影后仍然整。证明使用原仿射尾的整个 $R/(p)$ 模型；临界 normal 层虽然已有两份共同剩余因子，但真正的极化 jet 映射使原 $U_m\bmod p$ 在该层仍为零。

本结论不把投影后的特殊向量认作原向量，也不把 [R1201](R1201-original-highest-packet-kernel-log-unit.md) 的 packet 单位自动传给指定非 CM 商。末节明确保留同底向量不同整提升经过除 $p$ 后的返回。

## 1. 原对象与结论的量词

保持 R1018、R1021、R1193、R1195 的全部原来源。设
$$
p=12g-1>37,\qquad m=(p-1)/2=6g-1,\qquad
e_0=m(p+1),\qquad \pi_0^{e_0}=p.
\tag{1202.1}
$$
底环先取足够大的未分歧扩张 $W$，并置
$R=W[\pi_0]$；所需完备化沿原模型进行。记
$$
\Lambda=H^0(\mathscr X,\omega_{\mathscr X/R})
       =\omega_{\mathcal J/R}.
$$
原 compact-type 模型的这两个格相同，$\Lambda$ 为有限自由 $R$-模，并满足特殊纤维 base change；正则化的有理链不增加特殊 Hodge 空间。

仍以
$$
G=\operatorname{PGL}_2(\mathbf F_p),\quad
N=N_{\rm ns}/\mathbf F_p^\times,\quad
e_N=\frac1{2(p+1)}\sum_{n\in N}n
$$
表示原有限角。取 R1195 的准确整元素
$$
E=E_m=(e_{V_m}+e_{P_{m-1}})e_N,\qquad
U=U_m=p\,e_{V_m}e_N.
\tag{1202.2}
$$
它们由同一个原 full-$p$ 模型的实际 pull–push 实现；只在 $N$ 平均时反除 $2(p+1)$。所有 Weil 分支和原六标记下降保留。准确关系是
$$
E^2=E,\qquad EU=UE=U,\qquad U^2=pU.
\tag{1202.3}
$$
令 $q=U/p$，它首先只定义于泛纤维。

取原惯性及 deck 约定
$$
\sigma(\pi_0)=\xi\pi_0,\qquad \xi^{e_0}=1,\qquad
\delta(b)=\zeta^2b,\qquad\delta(u)=\zeta u.
$$
本篇对每一个**已给定的实际整微分**
$$
\Omega\in E\Lambda,\qquad
\sigma^*\Omega=\xi^{m^2}\Omega,\qquad
\delta^*\Omega=\zeta^2\Omega
\tag{1202.4}
$$
证明
$$
\boxed{\quad U\Omega\in p\Lambda,\qquad
q\Omega\in E\Lambda.\quad}
\tag{1202.5}
$$
其特殊纤维自动只在原 generic supersingular 尾的最高 Hodge 层；这是 R1193 的同一权 $m^2$。不要求另选一个有理商，也不更换原点 $D_0$。

## 2. 全部所需 polynomial normal 模

在本节 $k$ 是剩余域。令 $V_d=\operatorname{Sym}^d(k^2)$，并置
$$
D_N=(N+1)(p-1)-2,\qquad
M_N=V_{D_N}\otimes\det^{\,1-m}.
\tag{1202.6}
$$
这里 $N$ 为非负整数指标，不是正规化子群。原 normal 的使用范围将是 $0\le N\le p$。

先证明准确的有限算子恒等式
$$
\boxed{\quad \overline U\,M_N=0
              \qquad(0\le N\le p).\quad}
\tag{1202.7}
$$
$\overline U$ 表示同一个整群环元素 $U$ 的模 $p$ 作用，不是任意选取的一个 nilpotent 算子。

### 2.1 完整 Dickson 统计

以
$$
C=X^pY-XY^p
$$
过滤 $V_{D_N}$。$C$ 的角色为 determinant。第 $j$ 层剩余次数为
$d_j=D_N-j(p+1)$，twist 为 $\det^{1-m+j}$。

对 $d_j\ge p+1$，其 quotient 由在 $\mathbf P^1(\mathbf F_p)$ 的评价给出真正的 principal-series 模。其两个组成因子如下。记
$$
W_a=\operatorname{Sym}^{2a}(k^2)\otimes\det^{-a}.
$$
完整列表是
$$
\begin{array}{c|c}
j\text{ 的范围}&\text{两个组成因子}\\ \hline
0\le j\le m-2&
 W_{m-1-j},\quad W_{j+1}\otimes\det^m\\
j=m-1&\mathbf1,\quad\operatorname{St}\\
m\le j\le p-3&
 W_{p-2-j}\otimes\det^m,\quad W_{j-m+1}.
\end{array}
\tag{1202.8}
$$
这些式子也可直接由次数模 $p-1$ 和 determinant twist 相加核出；不是把非终端的长度二 quotient 用到已经终止的过滤。

R1195 给 $E$ 在 $W_a$ 上唯一可能的非零角像为 $a=m-1$，且为一维。对 $0\le a\le m$，
$W_a\otimes\det^m$ 没有 Cartan 固定向量：所需单项式下标为
$a\pm(m+1)$，均不在 $[0,2a]$ 内。
通常 Steinberg 没有正规化子固定向量。$\operatorname{St}\otimes\det^m$ 的 Cartan 固定线被另一 normalizer 陪集作用为 $-1$，因为本篇 $p\equiv3\pmod4$；所以它也没有 $N$-固定向量。

必须另记 terminal：

- $0\le N\le m-1$ 时，$j_{\max}=N$；终端是 $W_{m-1-N}$。
- $m\le N\le p-1$ 时，$j_{\max}=N-1$；终端次数
  $2(p-1-N)$，合 twist 后为
  $W_{p-1-N}\otimes\det^m$。
- $N=p$ 时，$j_{\max}=p-2$；终端为
  $\operatorname{St}\otimes\det^m$。

因此在 $0\le N\le p-2$ 中，仅 $j=0$ 给一份 $E$ 可见的 $W_{m-1}$。尤其 $N=p-2$ 时潜在的第二位置 $j=p-3$ 只剩次数二，已经 terminal，不能再取其不存在的第二组成因子。

在 $N=p-1$ 和 $N=p$ 时，$j=p-3$ 的剩余次数分别为 $p+1$、$2p$，第二份 $W_{m-1}$ 才真正出现；两个 terminal 均无 $N$-固定向量。因整幂等元取像 exact，
$$
\dim E M_N=
\begin{cases}
1,&0\le N\le p-2,\\
2,&N=p-1,\ p.
\end{cases}
\tag{1202.9}
$$
在第一行上，$\overline U^2=0$ 已迫 $\overline U=0$。第二行须真正拆开，不能仅凭维数认定其秩为一。

## 3. 临界两层的实际极化 jet 映射

取
$$
s=p-3,\qquad D=D_N,\qquad N\in\{p-1,p\}.
$$
此时
$$
\begin{array}{c|c|c|c}
N&D&D-s&D-(s+1)(p+1)\\ \hline
p-1&p^2-p-2&(p-1)^2&0\\
p&p^2-3&p(p-1)&p-1.
\end{array}
\tag{1202.10}
$$
并且 $D\bmod p$ 分别为 $p-2,p-3$，均至少为 $s$。

定义齐次极化
$$
\Delta_sF(X,Y;A,B)
=[t^s]F(X+tA,Y+tB).
\tag{1202.11}
$$
其 $X,Y$ 次数为 $D-s$，$A,B$ 次数为 $s$。在 $X,Y$ 的每条
$\mathbf F_p$ 有理直线上取任一非零代表评价。由于 $D-s$ 是 $p-1$ 的倍数，评价与代表无关，给真正的 $G$-映射
$$
\mathcal J_s:V_D\longrightarrow
V_s\otimes k[\mathbf P^1(\mathbf F_p)].
\tag{1202.12}
$$
这里对 polynomial variables 与 projective evaluation 同时运输；后一因子是原普通置换表示，没有另添 character 或 dual twist。

在直线 $(0,1)$，若 $F=\sum_j c_jX^jY^{D-j}$，则
$\Delta_sF(0,1;A,B)$ 中 $A^jB^{s-j}$ 的系数为
$$
c_j\binom{D-j}{s-j}\qquad(0\le j\le s).
$$
这些二项式全部是 $p$ 单位。因此该评价为零，准确等价于 $F$ 在该 projective 点消失至阶 $s+1$。在全部点同时使用，得到
$$
\ker\mathcal J_s=C^{s+1}V_{D-(s+1)(p+1)}.
\tag{1202.13}
$$
源减核的维数恰为 $(s+1)(p+1)$，等于目标维数，故 (1202.12) 满射。整个证明只用了已显示的单位因子，没有用一个未支付的高阶 evaluation 单射。

加上同一 $\det^{1-m}$ 后，两层 kernel 分别为
$\det^m$ 与 $\operatorname{St}\otimes\det^m$；两者均被 $e_N$ 杀掉。另一方面
$$
k[\mathbf P^1(\mathbf F_p)]=k\mathbf1\oplus\operatorname{St}
$$
是实际 $G$-直和，因为 $p+1$ 可逆。于是
$$
E M_N\simeq
E W_{m-1}\ \oplus\
E\bigl(W_{m-1}\otimes\operatorname{St}\bigr).
\tag{1202.14}
$$
第一项一维；(1202.9) 迫第二项也一维。它们来自两个真正的
$G$-子模，所以原 $\overline U$ 保持两项。由
$\overline U^2=0$，它在每条一维线上都为零。这证明临界两层上的 (1202.7)，并完成全部 $0\le N\le p$ 的算子消去。

## 4. 同一原曲线的全部 tail normal 都在这些模内

本节只使用 R1021 的实际 full-$p$ 仿射图在**整个非约化**
$R/(p)$ 上的常数化及常线性 level 作用。它不把紧化曲线或 node 整体宣称常数，也不读取未知的模 $p^2$ 变形。

原 $\Omega$ 的中心特殊约化为零，所以中心的首 normal 阶至少为一。在各原 generic 尾与三个 CM 尾，对 $0\le n<e_0$ 逐层读取 $\Omega$：

1. generic 尾的所有仿射 differential 惯性权为 $m$ 的倍数，因此只有 $n=Nm$ 能出现。
2. CM 尾的权为 $3m$ 的倍数，因此还须 $N\equiv2\pmod3$。本篇 $N\le p$，最后可能位置仍在已证明的有限区间。
3. 所有节点单位和 pairing 分支依 R1193/R1197/R1199 原式运输。有限 level 作用固定基底与 $\pi_0$，所以 $U\bmod p$ 可逐 normal 层施加。

为核完整 polynomial 次数，而不仅核最高项，设中心某层是
$\pi_0^h c\,w^j\,dw$，$h\ge1$。

| 原尾 | node 厚度 | 当前 $n$ 层尾上的最大极阶 | full 分支到该尾的无穷分歧指数 |
|---|---:|---:|---:|
| generic | $1$ | $n$ | $2$ |
| CM | $3$ | $(n+2)/3$ | $6$ |

第一行由 $n=h+j+1$、尾极阶 $j+2$；第二行由
$n=h+3(j+1)$ 给出。真正节点参数的单位不改变极阶，且原两种 full 分歧指数已由 R1030/R1197 保持。两行拉回 full 支后，differential 的极阶都至多 $2n-1$。

原 full differential $\eta$ 的无穷零阶为 $p-2$。因此当前层写为
$f_N\eta$ 时，$f_N$ 的极阶至多
$$
2n-1+(p-2)=2n+p-3=D_N.
\tag{1202.15}
$$
$n=0$ 的 generic 最高全纯微分同样给次数 $p-3=D_0$。

这也控制全部低极部及 holomorphic 自由项。由原光滑平面闭包的超平面正合列，每个这样的 affine coefficient 有总次数至多 $D_N$ 的 polynomial representative。再以同一 framing 在 $\mu_{p+1}$ 上平均，并用 $C$ 齐次化，原 norm/Weil 运输准确给
$$
c^{1-m}\operatorname{Sym}^{D_N}(k^2),
$$
即 (1202.6) 的同一个 determinant twist。这里的 $c^{1-m}$ 只在实际非零 pairing 分支上解释；不在 $c=0$ 的 evaluation 点代入它。

这就是 R1197 §4、R1199 §2.2 的原 polynomial 来源，现把纯极阶计算延长至 $n<e_0$。没有把旧 $\Theta^NF$ 的阶乘公式延至越过其消失位置；临界层改由 §3 的真实 jet 映射处理。

中心较高 normal 项、其它尾返回及当前层 holomorphic 修正，均仍属于上述完整 coefficient 模。节点 residue 为零；原 compact-type 树的有理链可在同一 dualizing 计算中合同，不产生另一个 pole 源。故 (1202.7) 逐层给
$$
\boxed{\quad
(U\Omega)|_{\text{每个 positive-genus tail 的仿射开}}
\equiv0\pmod p.
\quad}
\tag{1202.16}
$$
这一步尚未仅凭仿射消失宣称全局可除 $p$；剩下的中心可能项在下一节支付。

## 5. 可能的中心项也必为零

假设 $U\Omega\notin p\Lambda$。因 $\Lambda$ 自由，可取最小全局阶
$0\le h<e_0$，写
$$
U\Omega=\pi_0^h\Omega',\qquad
\Omega'\in E\Lambda,\qquad\overline{\Omega'}\ne0.
\tag{1202.17}
$$
由 (1202.16)，$\overline{\Omega'}$ 在所有 positive-genus 尾上均为零；有理链不贡献全局 Hodge。故其非零约化必须是中心的一条全纯 differential。

R1193 (1193.9) 给同一个整 packet 的特殊晶体权
$$
\pm m^2,\qquad\pm(m^2-1)\pmod{e_0}.
$$
中心权只能为 $p+1$ 的倍数，所以在本处只可能是
$m^2-1$ 或 $(m+1)^2$。

前者的整个全纯空间是 $k\,db/u$，deck 角色为 $\zeta$，与本篇 $\zeta^2$ 相反，故不能出现。后者的全纯空间可直接在原
$$
u^m=r^{2g}A_p(b),\qquad r=1-b^3
$$
上计算：
$$
H^0(I,\Omega^1)_{u\text{ 角色}}
=
\left\{\frac{uT(b)}{rA_p(b)}\,db:
          \deg T\le m-2\right\}.
\tag{1202.18}
$$
确切地，在 SS 点该基 differential 阶为零，在三个 CM 点为
$2g-1$，在无穷点为 $m-2$。有限处不允许更多分母，因而给所示完整次数界。其负 deck 部分另要求
$T\in b^2k[b^3]$；以下只用较弱的次数界。

由 $\Omega'$ 的权，唯一可能的 $h$ 是
$$
h\equiv m^2-(m+1)^2=-p\pmod{e_0},
\qquad h=e_0-p.
\tag{1202.19}
$$
若 (1202.18) 在某个 $s\in S$ 的 $T(s)$ 非零，它在该原 ordinary node 的中心参数 $w$ 中有非零常数项 $c_s\,dw$。厚度一的真实 node
$zw=\rho_s\pi_0$ 将它送到尾上的
$$
-c_s\rho_s\,\pi_0^{h+1}z^{-2}\,dz,
\qquad
h+1=e_0-p+1=2m^2<e_0.
\tag{1202.20}
$$
所有显示外因子均为原单位。因为 $h$ 是第一非零全局层，此处没有更早中心层产生同一 pole；更高层只给较低极阶，不能抵消其 $z^{-2}$ 系数。这与 (1202.16) 矛盾。

所以 $T(s)=0$ 对全部 $m-1$ 个简单 SS 根成立，而
$\deg T\le m-2$。于是 $T=0$，再次与
$\overline{\Omega'}\ne0$ 矛盾。故 (1202.17) 不存在，证明 (1202.5)。

本证明沿原完整 Hodge 格取最小全局阶，未把有限 normal 的 affine 消失直接替成一个未证的 global division，也没有遗漏节点或有理链上的 section。

## 6. 同一惯性角色格上的真正整幂等元

把原最高角色的整格记为
$$
\Gamma=
\{\Omega\in E\Lambda:
  \sigma^*\Omega=\xi^{m^2}\Omega,\ 
  \delta^*\Omega=\zeta^2\Omega\}.
\tag{1202.21}
$$
这是相对于未分歧 $W$ 的格，不称为整个 $R$-模 $E\Lambda$ 的 direct summand。由 (1202.5) 及 $q$ 与原惯性、deck 的交换性，
$$
q\Gamma\subset\Gamma,\qquad
\boxed{\quad\Gamma=q\Gamma\oplus(1-q)\Gamma.\quad}
\tag{1202.22}
$$
所以在这个实际角色格上，单尖点投影现已是整幂等元。

这不改写 R1195 的全角。该角里的 $(1,0)$ 仍不整；本篇证明的是它在 (1202.21) 这个原几何子格上的作用确实整。也不等于已证明它保存整个原 $R$-Hodge 格。

## 7. 原提升与指定两列的剩余问题

必须保留 (1202.4) 中的实际 $\Omega$。不能直接把
$\overline{q\Omega}$ 命名为只依赖 $\bar\Omega=L$ 的规范映射。

确切地，设 $\Psi$ 是负 deck、权
$b=(m+1)^2=m^2+p$ 的实际整 Hodge 提升。则
$$
\Omega\longmapsto\Omega+\pi_0^{e_0-p}\Psi
\tag{1202.23}
$$
保同一个最高权、同一个底 $L$。但是
$$
q\bigl(\pi_0^{e_0-p}\Psi\bigr)=\pi_0^{-p}U\Psi.
\tag{1202.24}
$$
右边由本篇确实整；其 generic 最高特殊分量却仍可能非零。若
$U\Psi$ 在该分量首项为 $\pi_0^p C$，它正返回 $C$，不能用
R1196 在除 $p$ **以前**的 lift 独立性删除。

因此当前已成和未成的边界是：

- 对每一个实际最高权整微分，$q\Omega$ 的整性及同角色格的整分裂已成。
- $q\Omega$ 的真正特殊向量、原 CM 各 normal 列以及同一 $\beta$ 的配对，仍须通过这个实际算子读取。
- R1201 已付的 $V_m(T_*)$ 是原 $E_m$ packet 的单位；本篇没有把
  $V_m(q\Omega_*)$ 设为该值，也没有把它自动送到 R1191 的指定
  $C$。
- 整性与原 R1190 的子簇 Lie 格界不是同一命题；两者没有被无说明相加或相互替代。
- 真正 whole-disc 及 Serre 绝对一致性结论仍开放。

## 8. 来源与证明范围

- R1018 §§1–2、R1021 §§2–3：原 compact-type Hodge 格、两种尾、完整惯性与整个 $R/(p)$ 的真实仿射模型及 level 作用。
- R1193 §§2–5、R1195 §§3–7：原 $E_m,U_m$、共同剩余因子、全部角归一及真实几何 pull–push。
- R1197 §4、R1199 §2：同一个 full polynomial coefficient 来源及 node 极界；本篇对新 normal 区间逐项重算次数，没有延用越界的参考导数。
- §3 的极化 jet 映射、kernel、满射和实际直和均已在正文自证，不依赖一个未证明的表示分裂或仅维数论证。
- R1196、R1201：同一原 log 的先整 packet 投影、有限 Čech 来源及完整 kernel 单位；本篇保留其量词与未付的纯型运输。

全文为纸面证明，未执行数学程序，未重扫既有素数窗口。root 与 o2_high_coefficient 独立核过临界极化 jet 的单位因子、两个 kernel、两条一维角上的 $\overline U$ 消失；这些核对不是额外授权或停工条件。
