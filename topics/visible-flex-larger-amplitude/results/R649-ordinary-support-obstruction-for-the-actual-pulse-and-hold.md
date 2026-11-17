# R649 — 同一 pulse/hold 前缀的实际普通支持量障碍

2026-11-17，constructive_model。**已证明的有限实际结论：** 对同一26e53规范化像 $G$，保存节点 $s=.8,\phi=\pi/2$ 的原点支持量严格为负。对它与准确下镜像组成的连通活动带，任意共同中心、任意连续一致法向选择都不能使普通支持量处处为正。该结论只排除以本活动带直接消费邻题R10的普通正径向支持工具；它不否定实际 reach、不否定内向闭合，也不排除新的加权支持工具。

## 1. 同一有限场与精确的轴向读数

输入为 R648 的 `parallel-pulse-a5-complete-base.json.gz`，SHA256
`26e53e8cdbdf6205a8bd9b2976cd4bcd36ad8734b0aca69512d705d826c5af72`。
保存的全部二 jet 定义同一准确共同五次场；此次只读取7个已有节点的两个反射轴，没有扫描新径向/角网格，没有替换保存的速度为ODE RHS。

在固定旋转标架中写 $F=(R,T,Z)$。R/Z为常数加 $\cos(2j\phi)$，T为 $\sin(2j\phi)$。在 $\phi=0,\pi/2$ 上所有正弦准确为0，余弦准确为 $1$ 或 $(-1)^j$，所以 R/Z/径向速度及 $c=Z_0,c_s$ 都可对保存 binary64 系数作准确有理求和。$F_\phi=(0,d_T,0)$，其中

$$d_T=R+T_\phi.$$

本次全部14点的 $R,d_T$ 均准确严格正，故 $N=F_\phi\times F_s$ 的单位法向在轴点为

$$n=(Z_s,0,-R_s)/\sqrt{R_s^2+Z_s^2}.$$

轴上原点支持的分子为 $D=RZ_s-ZR_s$。

## 2. 实际归一化及 $\lambda_s$ 的抵消

使用已经登记的同一 $G=c e_z+\lambda(F-c e_z)$，没有改用 raw 支持作结论。设 $l=\lambda_s$；轴上

$$G_R=\lambda R,\quad G_Z=c+\lambda(Z-c),$$
$$G_{R,s}=\lambda R_s+lR,\quad
G_{Z,s}=Z_s+(\lambda-1)(Z_s-c_s)+l(Z-c).$$

实际 $G$ 的 meridian 支持分子准确为

$$\boxed{D_G=G_R G_{Z,s}-G_ZG_{R,s}
=\lambda^2D+\lambda(1-\lambda)(Rc_s-cR_s)-l cR.}$$

这里含 Z 的两个 $l$ 项准确抵消，不能丢弃剩余 $-lcR$。

R648的完整单片报告已给同一场、同一精确标量、同一构造N4096上的全径向界
$|\lambda-1|\le\epsilon$、$|l|\le\epsilon_1$。因此用准确有理数计算

$$E=(2\epsilon+\epsilon^2)|D|+(1+\epsilon)\epsilon|Rc_s-cR_s|
   +\epsilon_1|cR|$$

便有 $D-E\le D_G\le D+E$。本次每点选取实际包含该准确节点的已完成闭片报告，检查其输入/来源/哈希；未重新求 $\lambda$。所有表格端点向外取整，输出另保存准确有理端点。

## 3. 实际结果

下表为 $\phi=\pi/2$ 的实际 $D_G$ 区间，表中数值再次向外放宽；另一轴的7点均严格为正（最小分子大于1.36）。

| 保存节点s | $D_G$ 的严格包围 |
|---|---|
| 0 | $[.4541187684608,.4541187684611]$ |
| .5 | $[.2665966268767,.2665966268774]$ |
| .8 | $[-.0091538647817,-.0091538647807]$ |
| .95 | $[-.1835749345372,-.1835749345360]$ |
| .99 | $[-.0997208707983,-.0997208707613]$ |
| .995 | $[-.0840510294827,-.0840510294014]$ |
| 1 | $[-.0866887072834,-.0866887071200]$ |

R648已付实际浸入，且轴上 $d_T>0,\lambda>0$，故 $D_G<0$ 的点具有严格负的单位法向支持，而非只看到一个未定向叉积为负。节点.5的轴点正不表示整段/全角正，更不说明达到所需支持下界；此次没有外推首次变号位置。

## 4. 任意共同中心的完整障碍

实际有限谱严格满足

$$G(s,\phi+\pi)=QG(s,\phi),\qquad Q=\operatorname{diag}(-1,-1,1).$$

对同一输入第0节点的字面检查还给
$Z=0$、$F_s=e_z$、$(F_{ss})_Z=0$，对应所有系数准确为0/1。复现断言是

```python
m = d['M']
y, v, acc = (d[key][0] for key in ('states', 'rhs', 'd2'))
assert all(z == 0.0 for z in y[2*m+1:])
assert all(z == 0.0 for z in v[:2*m+1])
assert v[2*m+1] == 1.0 and all(z == 0.0 for z in v[2*m+2:])
assert all(z == 0.0 for z in acc[2*m+1:])
```

原精确标量 $a_s(0)=0$，故 $b_s(0)=\lambda_s(0)=0$。沿R644§5的同一证明，准确下镜像 $G(-s,\phi)=J G(s,\phi)$、$J=\operatorname{diag}(1,1,-1)$ 给C²接合。由于径向参数也取负，法向满足 $N(-s,\phi)=J N(s,\phi)$。合并半转后

$$G(-s,\phi+\pi)=-G(s,\phi),\qquad
n(-s,\phi+\pi)=-n(s,\phi).$$

取上述任一负支持点 $p$ 及其准确反点 $-p$。对任意 $c_*\in\mathbb R^3$，

$$(p-c_*)\cdot n(p)+(-p-c_*)\cdot[-n(p)]=2p\cdot n(p)<0.$$

二者不可能同时为正，水平/竖直中心平移都不能修复。若把全局法向反向，核心第0节点的严格正支持点及其反点在新法向下具有负支持，同样排除全部共同中心。连通活动带的连续一致单位法向只有这两个选择。因此任何保留这整个镜像活动带的C²闭合，都不能满足普通正支持R10的前提。

这不是所有 reach 证明的障碍。非镜像下片、改变原前缀、不同的支持向量场或直接完整几何 reach 证明均不被本条排除。对原 aa1 hold 候选，R644已证明旧498胞与同一精确标量完全相同；本条.8/.95见证在这个共同旧段内，故同一普通支持障碍原样适用，不必再扫描hold。新有限BVP/LM改变过的前缀不由此自动排除。

## 5. 最小源与实际证据

冻结源 `parallel-model-axis-support-probe.py`，4284B，SHA256
`f05c217dd81276799504203a658031209df25a3f58eab24e81e2568c0391476e`。
固定目标为 `0 .5 .8 .95 .99 .995 1`，选取已有最近节点，实际恰为这些节点；两个轴共14点。只作准确有理运算和每点一次有理平方根上包围；没有有限角采样近似正弦/余弦。

实际报告 `parallel-model-pulse-axis-support-probe.json` 的SHA256为
`828ad538cae8b9e44076246705533bc44e285854ccbead67d3277f0aba9cbfbe`。
依赖完整Gram终态 `df41433b71147ac11d3f0193be31323d7e23a879cb2b05231d3a3e166b0d88fb`；所消费每份已有单片报告的路径/完整SHA逐条保留。源与证明入库，raw报告留仓库外。

```sh
PYTHONDONTWRITEBYTECODE=1 python "$WORK/parallel-model-axis-support-probe.py" \
 --input "$WORK/parallel-pulse-a5-complete-base.json.gz" \
 --gram-result "$WORK/parallel-pulse-gram-fixed-recovery/result.json" \
 --targets 0 .5 .8 .95 .99 .995 1 \
 --out "$WORK/parallel-model-pulse-axis-support-probe.json"
```

独立正在运行的原818胞曲率批没有改动；本次没有开启普通支持全域扫描，也没有用这一工具障碍暂停主课题。

仓库中的规范源码为 [2026-11-17-parallel-model-axis-support-probe.py](../notes/2026-11-17-parallel-model-axis-support-probe.py)，与上述冻结f05c源逐字相同。
