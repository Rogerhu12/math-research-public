# R892 — 原双映射的完整 PARI 有理基与认证不变性

**状态：已证明（基更换与严格认证不变性）；生产脚本已提交，尚未取得本路径的完整计算回执。**
日期：2026-11-16。原两条映射、原 Hecke 方向及所有绝对归一化均取 R874/R875/R878；本条只更换完整模形式空间的计算基，并采用 R889 已证明相同的有限 Newton germ。它不证明原端点非零、ordinary 局部化非零或主目标。

## 1. 完整有理空间及精确构造器

令
$$
\mathcal M_k=M_k(\Gamma_0(867),\mathbf Q).
$$
本题已固定的基曲线指标为 $1224$、亏格为 $85$、尖点数为 $36$，没有椭圆固定点。因此
$$
\dim\mathcal M_2=85+36-1=120,\qquad
\dim\mathcal M_k=102k-84\quad(k\ge4\text{ 偶数}),
$$
且权 $k$ 的普通 Sturm 上界为 $102k$。这些数也正是旧两个 producer 采用的空间和上界。

PARI 的官方 modular-forms 文档明确：完整空间由 flag $4$ 初始化；其 mfbasis 的系数在 nebentypus 的值域 $\mathbf Q(\chi)$ 中，而非 eigenbasis 可能需要的扩大域。故输入
$$
\operatorname{mfinit}([867,2,1],4)
$$
给的是 $\mathcal M_2$ 的有理基。mfcoefs 直接作用于该空间时，所得矩阵的列正是同一个 mfbasis 中各形式的 Fourier 系数。构造器不是从任意有限 q 串认模形式。

本条实现只建立一次该空间，立即检查 level/weight/character/flag 为 $(867,2,1,4)$、维数及基长度均为 $120$。整个生命周期保留同一个空间对象。任何扩大精度的 mfcoefs 调用必须逐项重现全部旧前缀；每个系数都经精确 QQ 转换，任何非有理项使程序失败。

为重放固定 Docker 镜像，并在 mfinit 紧前固定 PARI seed；结果元数据记录 PARI 版本、seed、构造式、helper 的 SHA-256 及原有完整低基 SHA-256。不把 PARI 的第 $i$ 个基元认作 Sage 旧基的第 $i$ 个基元。

## 2. 原乘积基规则对这个完整基仍严格有效

令 $b_1,\ldots,b_{120}$ 为上述完整有理基。权 $2r$ 的所有候选是已经存在的、真实模形式
$$
b_{i_1}\cdots b_{i_r}\in\mathcal M_{2r}.
$$
继续采用旧 producer 的逐批 rank/pivot 选择：只在分母可逆的有限素数处读取从 $Q^0$ 至 $Q^{102(2r)}$ 的全部系数，并且只在独立行数**实际等于**
$$
102(2r)-84
$$
时接受该乘积基。

证明：所取行的一个相应阶子式在有限域非零，故原有理子式也非零，得到同数目的有理线性无关形式。该数等于整个空间维数，因此所取形式是完整基。没有达到该数时程序直接失败，不据部分搜索声明张成。归纳使用上一完整权空间的已选乘积，所以实现中有限的候选生成方式也不改变该论证。这里不需要假设某个预先固定的乘积子集张成。

权二自身同样保留旧的前 $205$ 项 rank $120$ 检查。该检查是构造器输入后的准确独立性门，不是以 q 串替代模性。

## 3. 两个原重建问题都不随完整基更换改变

### 3.1 原 P 映射

固定原
$$
u=(915,1097,2962)/55569,\qquad
\lambda=(68+7\sqrt[3]{17}-13\sqrt[3]{17}^{\,2})/3,
$$
以及 R874/R875 的 $v_{\rm new}=\lambda^3v$、$H_u/\lambda$，不作新的选择。写 $H_u(q)/\lambda=qf(Q)$、$Q=q^3$，则 $f(0)=1$。对每个旧权 $k\in\{4,6\}$，候选仍为
$$
Y_{\rm new}=A/B,\qquad A,B\in\mathcal M_k.
$$
任两个完整基间的变换在 $\operatorname{GL}_{\dim\mathcal M_k}(\mathbf Q)$ 中。它只改变 $A,B$ 的坐标，不改变这个有理函数候选集合、原微分条件或尖点支。

新基下的有限 echelon 自由坐标和 CRT 高度可能与旧基不同，所以必须重新求原有限矩阵、全部三个 $\sqrt[3]{17}$ 嵌入、共同 pivot 型及有理重建。旧坐标、旧矩阵 hash 或某一有限解都不被搬入新基。

接受仍要求同一特征零的全恒等式
$$
C^3-hA^2(A+v_{\rm new}B)^2B^2=0,\qquad
C=(Q A')B-A(Q B'),\quad h=Qf(Q)^3=(H_u/\lambda)^3,
$$
完整核至原 $612(k+1)$ 上界，及旧首项、旧微分和基点门。R875 的 Sturm/原映射唯一性证明因此逐字适用。整数 Hecke 返回 $17$ 和全部原 Artin 来源没有变化。

### 3.2 原 F 映射

固定原 $E_{17}:y^2=x^3+17$ 的 normalized newform $f(q)=qf_0(Q)$、$Q=q^6$ 与绝对 eta 乘子；记 $\eta_{\rm unit}(Q)=\prod_{n\ge1}(1-Q^n)$。对每个旧权 $k\in\{2,4\}$，候选仍为
$$
V=A/B,\qquad A\in\mathcal M_{k+6},\quad B\in\mathcal M_k.
$$
分别更换两个完整基，不改变这个候选集合。必须重新计算其真实矩阵和 CRT；尤其不能把 P 路径与 F 路径的基序号混用。

原完整认证仍为
$$
8\Delta C^3=HB^2(A^2-17\Delta B^2)^2,
$$
其中
$$
C=(QA')B-A(QB')-\tfrac12E_2AB,
\quad \Delta=Q\eta_{\rm unit}^{24},
\quad H=Qf_0^3\eta_{\rm unit}^{12}.
$$
保留 $V(0)=-1,[Q]V=5$、原微分 $dx/(2y)=f(q)dq/q$、无穷点送 $O$，以及至 $612(k+6)$ 的全部原特征零核验。R878 的认证与唯一性证明仍成立，不引入 Manin 常数 $1$ 假设。

因此，两条新路径只要各自实际通过旧完整门，就各自给出旧问题要求的同一原映射；若超时、有限预算耗尽、基秩不足或某项恒等式失败，则没有给出该映射的认证。

## 4. 生产实现与消费约定

新增实现：

- scripts/original_pari_m2_basis.py：同一 PARI 对象的整矩阵扩展，QQ 强制与全部旧前缀一致性；给原程序需要的 q_expansion 接口。
- scripts/produce-r892-original-rational-hecke-map-pari.py：从 R889 原 P producer 只改完整 M2 提供者及来源元数据。
- scripts/produce-r892-original-first-factor-map-pari.py：对应原 F producer 的同样变更。
- .github/workflows/rank2-sha-original-maps-pari.yml：两个独立原任务，固定原 Sage 10.6 镜像，无网数学容器、只读源码挂载；最长任务时间与旧生产路径相同。
- ci/original-maps-pari-request.json：这次路径的参数与用途记录。

R889 的 Newton germ、所有旧矩阵形状/权/prime/CRT 预算、原 source coefficients、初始 char0 校验、全末端认证均保留。既有旧递推任务和 Sage 基的 Newton 任务继续运行。

同进程消费必须使用该 producer 自己的 forms2、recipes_by_power、实际认证坐标与权，或完全重放指定源码；不能跨提供者搬坐标。尚未取得两个真实 PASS 及完整 RR 前，不发送原 shadow consumer 请求。

所有数学执行仅在公开 Actions。没有在本地或代码编排器执行任何数学检查。按根规则15，不提交系数/矩阵/证书输出或 artifact，只保脚本、参数、run 与输出 SHA-256。由于旧任务尚未返回日志，本条不声称已测得 Sage 基构造是超时原因，也不预报 PARI 路径的速度或 PASS。

## 5. 来源

- PARI/GP Development Team, *Catalogue of GP/PARI Functions — Modular forms*, 官方在线手册，2026-11-16 读取：[空间及有理系数、mfbasis、mfcoefs、mfinit、mfparams](https://pari.math.u-bordeaux.fr/dochtml/html-stable/Modular_forms.html)。
- PARI/GP Development Team, *User's Guide to PARI/GP*, version 2.17.1, §§3.18.15 等：[官方 PDF](https://pari.math.u-bordeaux.fr/pub/pari/manuals/2.17.1/users.pdf)。整空间 mfcoefs 的列定义也见较早官方手册。
- 本仓库 R874/R875/R878、[R889](R889-original-two-map-newton-germs-and-exact-normalization.md)；原两 producer 的具体来源与当前 run 见 HANDOFF。
