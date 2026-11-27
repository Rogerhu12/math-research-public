# Phi=0 的 H1 余图：全局原首一六次组合与 14472 / 28944 有限点界

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。

## 1. 完成结论

仍在已付原单位、物理 $D\ne0$ 的 $\Phi=0$ 图上，限制到原第一头曲线
$$
g(u,Q)=-12H_{6,4}(u,Q)=0.
$$
沿用真实坐标 $v=Jf-G+bc\,z$，$z=Qt$。新三头 $h$ 的整个原值零支已经由
[R150-appendix-unit211-Phi-zero-H1-new-three-head-zero-complete-original-exclusion.md](R150-appendix-unit211-Phi-zero-H1-new-three-head-zero-complete-original-exclusion.md)
排除，所以当前剩余原解上 $h\ne0$。

**本次在同一个原方程理想中构造出一条首一的 $\lambda$ 六次式。** 其所有权分母仅为已经支付的原单位、h 及旧 C55 已排除的整 u 因子；没有留下新的六次首项零支。

结合原三生成元规则，得到：

- 每个剩余固定 $(u,Q)$ 的必要代数长度至多为 18，因而其 $(\lambda,T,v)$ 点数至多为 18。
- 已证剩余权对至多 804，所以 $(u,Q,\lambda,T,v)$ 的不同点总数至多为 14472。
- 每个五坐标点，完整固定规范原坐标至多有两种恢复，来自 $\rho^2=1-Q$ 的两个根。因此完整固定规范原点至多为 28944。

最后两个结论是不同点的界。没有把 P201 的不同权点上界提升为整个权 scheme 的长度，也没有宣称这些有限候选已经排空。

## 2. 从完整原二次式取得六个真实首项

四条已刊原式是清分母、仅剥原单位后的
$$
\widetilde R,\quad\widetilde W,\quad\widetilde O,\quad\widetilde N_1
\in \mathbb Q[u,Q]/(g)[\lambda,T,v].
$$
它们对 $(\lambda,T,v)$ 的总次数至多为 2。当前三头选 $(R,W,N_1)$；记其二次头矩阵为 H，$h=\det H$。原 adjugate 恒等式给三条规则
$$
hT^2=\mathbf v r_{20},\qquad
hTv=\mathbf v r_{11},\qquad
hv^2=\mathbf v r_{02}
\quad\pmod I,
$$
其中 $\mathbf v=(1,T,v)$，I 是四个完整原式生成的理想。

相应真实三列乘法矩阵满足
$$
\mathbf v M_T=hT\mathbf v,\qquad
\mathbf v M_v=hv\mathbf v\pmod I.
$$
令 r 是剩余完整原 O 的带 h 余列。于是以下五列都被同一个 $\mathbf v$ 模 I 消掉：
$$
c_0=r,\quad c_1=M_Tr,\quad c_2=M_vr,\quad
c_3=[M_T,M_v]e_T,\quad c_4=[M_T,M_v]e_v.
$$
第一列的 $\lambda$ 次数轮廓至多为 $(2,1,1)$，其余为 $(3,2,2)$。因此六个固定原 cofactor
$$
F_{ij}(\lambda)=\det[c_0,c_i,c_j],
\qquad 1\le i<j\le4
$$
对 $\lambda$ 的次数至多为 6。

这些 cofactor 不只是同解集必要式，也属于原理想 I。确切地，
$\mathbf v C_{ij}\in I^3$，右乘 $\operatorname{adj}(C_{ij})$ 后得到
$\det(C_{ij})\mathbf v\in I^3$；取 $\mathbf v$ 的第一个坐标 $1$，即得 $F_{ij}\in I$。
交换子列的同源关系直接由两条真实乘法身份相减给出，不假定三生成元模自由。

记
$$
L_{ij}=[\lambda^6]F_{ij}.
$$
本次只取四条完整原二次式的总二次齐次部分，再令其齐次 $\lambda$ 坐标等于 1，计算上述六个 L。这是取得首项的精确分次操作，不是把完整原解的 $\lambda$ 值设为 1。由列的权次数，齐次操作与这里的矩阵乘法及行列式恰给同一个 $\lambda^6$ 系数。

源对原头 adjugate 和齐次原关系逐项乘回。没有重建旧的完整 cofactor、旧结果式或 Dixon 消元。

## 3. 仅剥已付单位及完整正则 adjugate

对每个 L，源只尝试整除当前原图已付的权单位以及 h，每次在完整四个 Q 坐标上核对多项式乘积。实际
$$
L_{ij}=s_{ij}\ell_{ij},
$$
其中全部 $s_{ij}$ 如下：

| $(i,j)$ | $s_{ij}$ |
|---|---|
| $(1,2)$ | $h^2u^2(u-1)^{20}Q^{11}T_0^{18}$ |
| $(1,3)$ | $h^2u^2(u-1)^{19}Q^9T_0^{15}\ell_n$ |
| $(1,4)$ | $h^2u^2(u-1)^{18}Q^{10}T_0^{15}\ell_n$ |
| $(2,3)$ | $h^2u^2(u-1)^{18}Q^{10}T_0^{15}\ell_n$ |
| $(2,4)$ | $h^2u^2(u-1)^{17}Q^{11}T_0^{15}\ell_n$ |
| $(3,4)$ | $h^2u^2(u-1)^{18}Q^9T_0^{14}$ |

这里
$$
\ell_n=Q-2(u-1)(u-2)=Q\ell,\qquad
T_0=-Q-4(u-1).
$$
h 的非零性只来自已刊完整原值排除，并未把它的范数当成原单位。

对完整 Q 四维代数中乘 $\ell_{ij}$ 的正则矩阵取行列式及第一 adjugate 列，得到
$$
\ell_{ij}a_{ij}=N_{ij}(u).
$$
每个式子在全部四个 Q 坐标中完整乘回。其实际 QQ 范数次数依次为
$$
182,\quad160,\quad168,\quad168,\quad176,\quad146.
$$
这里范数用于形成多项式恒等式，没有被反演。

源对六个 $N_{ij}$ 求完整 QQ[u] Bézout，得到首一共同因子 C 和多项式 $b_{ij}(u)$：
$$
\sum_{i<j}b_{ij}(u)N_{ij}(u)=C(u).
$$
五次 Bézout 的原乘积均返回。再接正则 adjugate，完整四坐标目标恒等式是
$$
\boxed{
\sum_{i<j}b_{ij}(u)a_{ij}(u,Q)
\frac{L_{ij}(u,Q)}{s_{ij}(u,Q)}
=C(u).
}
$$
这是在只倒置已经支付的 $s_{ij}$ 的原权环中的恒等式。

## 4. C95 的全部零支已经支付

本次精确得到 $\deg C=95$，规范系数身份为 3683 字节，SHA256：
aa988275c3063d03383f77ab79b6a013aaca7d00627f42c1b85dedbf28ec357c。

完整 QQ 因式分解及乘回给
$$
\boxed{
C(u)=u^{26}(u-1)^{22}
(u-\tfrac32)^{14}
(u-\tfrac{12}{5})^9
(u-\tfrac52)^9 H_5(u)^3,
}
$$
其中
$$
H_5(u)=u^5-\tfrac{83}{12}u^4+\tfrac{349}{18}u^3
-\tfrac{995}{36}u^2+20u-\tfrac{52}{9}.
$$
$H_5$ 的规范系数身份为 46 字节，SHA256：
5014dd28e57ecbdb07b887120ecffdba955db61581b8eed648e1335990217240。

$u=0,1$ 由原单位排除。三个一次纤维已经由
[R150-appendix-unit211-Phi-zero-H1-three-linear-poles-complete-exclusion-and-1012-cover.md](R150-appendix-unit211-Phi-zero-H1-three-linear-poles-complete-exclusion-and-1012-cover.md)
完整排除；整个 $H_5$ 纤维已经由
[R150-appendix-unit211-Phi-zero-H1-six-nonlinear-poles-complete-exclusion-and-804-cover.md](R150-appendix-unit211-Phi-zero-H1-six-nonlinear-poles-complete-exclusion-and-804-cover.md)
完整排除。

所以当前 H1 的所有剩余完整原解上，C 确为非零。没有因为某个模因式看似旧因子而删支；本次用的是 QQ 精确因式及与已刊因子相同的有理定义。

## 5. 同一个原理想中的首一六次与每权长度 18

定义
$$
\mathcal F(\lambda)=
\frac1{C(u)}
\sum_{i<j}b_{ij}(u)a_{ij}(u,Q)
\frac{F_{ij}(\lambda)}{s_{ij}(u,Q)}.
$$
由上一节，所有分母在当前原图上已经支付。因 $F_{ij}\in I$，$\mathcal F$ 属于同一原理想的此已付局部化。其 $\lambda^6$ 系数由完整目标身份恰为 1，且次数至多为 6。因此 $\mathcal F$ 是真正首一六次式。

若希望完全清回多项式，可取
$$
S=h^2u^2(u-1)^{20}Q^{11}T_0^{18}\ell_n.
$$
上表每个 $s_{ij}$ 都整除 S。于是
$$
SC\,\mathcal F
=\sum_{i<j}b_{ij}a_{ij}(S/s_{ij})F_{ij}
$$
是完整原多项式组合，其准确六次首项为 $SC\ne0$。这也明确保留所有分母的来源；不要求另行展开大系数载荷。

现在固定任何剩余权点 $(u_0,Q_0)$。$h(u_0,Q_0)\ne0$ 给 $T^2,Tv,v^2$ 的三条首一规则，所以该权点的原商在 $\mathbb C[\lambda]$ 上由
$$
1,\quad T,\quad v
$$
生成。再使用刚证明的首一六次 $\mathcal F$，整个必要商由
$$
\lambda^j,\quad \lambda^jT,\quad \lambda^jv,\qquad 0\le j<6
$$
共 18 项生成。因此它是维数至多为 18 的复代数，其 scheme 长度及不同点数均至多为 18。施加其它完整原条件或已付非零条件只会进一步取商或局部化，不增加这一有限长度。

已有不同权对数至多为 804，故不同五坐标点满足
$$
\boxed{
\#\{(u,Q,\lambda,T,v)\}\le804\cdot18=14472.
}
$$
这里没有把权点上可能存在的非约化重数计入 804，也没有由此断言全部权与值联合 scheme 的长度为 14472。

## 6. 完整固定规范坐标只有两个同源恢复

以下给出恢复公式，确认五坐标之外没有遗漏自由 Gram 参数。

对给定 $(u,Q,\lambda,T,v)$，先取
$$
\rho^2=1-Q.
$$
原 $1-Q$ 单位保证至多两个不同根。对每个根，
$$
p=1+\rho,\quad q=1-\rho,\quad
\ell=1-\frac{2(u-1)(u-2)}Q,\quad m=u-\ell,
$$
$$
b=\frac{\ell+m/\rho}{2},\qquad
c=\frac{\ell-m/\rho}{2}.
$$
这些是原权定义，不是新的拟合参数。

接着
$$
G=\lambda P_{02}+(u-1)T_0,\qquad
P_c=QP_{02}(\ell+T)-GT_0,
$$
$$
f=-P_c/P_f,\qquad
z=\frac{v-Jf+G}{bc},\qquad t=z/Q.
$$
$P_f,bc,Q$ 都已付。

令
$$
W_1=\frac{T_0+4uf}{2},\qquad V=v/Q.
$$
原 E0 与 N0 的同点两线准确为
$$
bpX+cqY=W_1,\qquad bX+cY=V.
$$
其行列式 $bc(p-q)=2bc\rho$ 非零，因此
$$
X=\frac{W_1-qV}{b(p-q)},\qquad
Y=\frac{pV-W_1}{c(p-q)}.
$$
原四个自由 Gram 条目唯一恢复为
$$
r=X-(1-\ell)p-ct,\qquad
s=Y-(1-\ell)q-bt,
$$
$$
A_{\rm Gram}=2f-2bX-2cY+2bc\,t,
$$
以及已经给出的 t。其它条目由原固定规范和对称 Gram 装配确定，没有再选一个 Gram 点。

还须保完整原值恢复。记
$$
A_2=2\lambda^2-2\lambda+1,\qquad
B_3=4\lambda^3-6\lambda^2+3\lambda-1,
$$
$$
D=\ell A_2-T^2,\qquad
K=\ell^2B_3-3\ell TA_2+2T^3,\qquad
M=\ell(2u-\ell Q)-u^2.
$$
在原值记号
$$
h_U=1+v_0-\rho\sigma,\qquad
k_U=1+v_0+\rho\sigma,\qquad \sigma=-v_1
$$
下，完整 HA/HB 两个矩条件给
$$
T=\ell v_0-m\sigma,\qquad D=M\sigma^2,\qquad
K=2mM\sigma^3=2mD\sigma.
$$
这些等式可直接由原二、三矩展开得到。当前 $D,\ell,m$ 均为原已付单位，故
$$
\sigma=\frac{K}{2mD},\qquad
v_0=\frac{T+m\sigma}{\ell},
$$
并且
$$
\zeta=v_0+\sigma
=\frac{T+uK/(2mD)}{\ell},\qquad
w=\lambda-1-T.
$$
所以 $h_U,k_U,\zeta,w$ 也都由同一个点唯一恢复。没有从单独 F6 的范数型方程选择一个额外平方根；这里使用的是完整原 HA/HB。

因此每个五坐标点至多给两个完整固定规范原点，只由 $\rho$ 的两个选择产生。B/C 交换恰与这种选择相容，不能再任意增加来源。得到不同点界
$$
\boxed{\#\{\text{当前 H1 完整固定规范原点}\}\le28944.}
$$
这个界只适用于本稿的原 $\Phi=0$、$D\ne0$、H1 余图，不外推到碰撞分支或一般原问题。

## 7. 唯一实际执行

源：
[2026-11-28-unit211-Phi-zero-H1-six-homogeneous-lambda-leading-original-target-8542.py](../notes/2026-11-28-unit211-Phi-zero-H1-six-homogeneous-lambda-leading-original-target-8542.py)。

- 源 blob：74b910b88e545e15a49a31768b2ad67cedab8584。
- SHA256：49ad639de88d8a9dd2eecf7fe2da9b294e3487b5ccf139cf6ba319694150439c。
- 唯一 run/job：46074334560 / 140758420507。
- source commit：08f5b23fc94f2452a84ff07485e46c29b5014859。
- 内层：0.998030146 秒 / 49952 KiB / exit 0。
- stdout：10926 字节，SHA256 3ec818639a11630232442da55ba8887ab9c349d1a485f2ed7bba1b2a648876ea。
- 实际 pull：2026-11-27 22:04:45 UTC，至 3f7b10c82523027d99e102b7b5172af409432a60；两份 README blob 未变化。

六个真实首项的原因子乘回、六个四维正则 adjugate 乘回、五次 QQ Bézout、完整四坐标 C 目标及 C 的全部 QQ 因式乘积均已实际完成。大系数只保身份，没有传输或入库可再生系数载荷。

首一六次与有限点界已经成立，不以之后的原理想排空计算作登记前置条件。当前普通不变子空间问题仍未完成。
