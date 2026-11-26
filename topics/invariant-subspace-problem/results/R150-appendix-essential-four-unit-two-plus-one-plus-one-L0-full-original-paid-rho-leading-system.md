# R150 / L0：已付完整 rho 首项后的原九式精确必要系统

作者：AI-assisted GPT-6 Astra Pro；Astra-ISP-8542378f-20261127；2026-11-27（台北）。

**状态：以下原必要系统与全部除法来源已证明，构造实际通过；一般 L0 尚未排除。** 本条使用整个 $W,G,K,V$ 曲线已经关闭这一实质新输入，保留原均值、$P/N$ 全部偶奇分量，并在有理数域运行一次完整原理想单位门。它没有重跑已失败的 $X/Y$ 大直接结式。

## 1. 原来源与同一个 t

沿用[整个 K 曲线](R150-appendix-essential-four-unit-two-plus-one-plus-one-L0-K-curve-complete-exclusion.md)和[整个 V 首项曲线](R150-appendix-essential-four-unit-two-plus-one-plus-one-L0-V-leading-rho-curve-complete-exclusion.md)的可逆原图。几何变量为 $\rho,\lambda,w$；源从双点 Frobenius 原乘法直接重建原九式

$$E_1,E_{B,e},E_{B,o},P_1,P_{B,e},P_{B,o},N_1,N_{B,e},N_{B,o}.$$

二重点积的第二坐标准确为 $v_0z_1+v_1z_0$；全部二次代数共轭、原三个 U 矩、$P(V)=N(V)=0$、原 $P_1$ 线性身份均在源中实际检查。各原系数分母只含已付物理单位，清分母时每个共同因子、常数及系数乘积全部乘回。

记原 $P_1=\alpha t+\beta$。已付 $\alpha\ne0$，故同一点唯一恢复为 $t=-\beta/\alpha$。对另任意一条原清分母式 $Q(t)=\sum_{j=0}^d q_jt^j$，定义

$$G_Q=\sum_{j=0}^d q_j(-\beta)^j\alpha^{d-j}.$$

有完整原组合

$$\alpha^dQ(t)-G_Q=(\alpha t+\beta)
\sum_{j=1}^d q_j\alpha^{d-j}
\sum_{h=0}^{j-1}(\alpha t)^{j-1-h}(-\beta)^h.$$

因此原九式在已付图上可由同一个 $t$ 返回；没有各自取不同根或仅对范数取零。源中的每个 $G_Q$ 只除已付因子，实际保存 $G_Q=(\text{已付因子})F_Q$ 的整除乘回。所有原偶奇行分别保留。

## 2. 整个 rho 首项和低次原组合

原 $F_E=F_{E_1}$ 是 $\rho$ 五次式。其首项为非零常数乘 $R^2WCV$，其中 $R,C$ 是原单位，整个 $W,V$ 零面均已排除。因此 $\operatorname{lc}_\rho F_E$ 是合法单位；源实际剥除全部已付因子后核验余项为非零有理常数。

再记 $F_N=F_{N_1}$，并令

$$R_4=\operatorname{lc}_\rho(F_E)F_N-\operatorname{lc}_\rho(F_N)F_E.$$

剥除已付因子后的 $R_4$ 对 $\rho$ 至多四次。源实际核验剥除因子乘 $R_4$ 等于上述原组合。本条将该低次关系作为辅助行加入，仍保留八条原返回行，避免用少数均值或投影替换所有 $P/N$。

次数依次为 $(\rho,\lambda,w)$：

| 原必要行 | 次数 | 项数 |
|---|---|---:|
| $F_{E_1}$ | $(5,15,16)$ | 978 |
| $F_{E_{B,e}}$ | $(7,20,17)$ | 1894 |
| $F_{E_{B,o}}$ | $(6,18,16)$ | 1455 |
| $F_{P_{B,e}}$ | $(10,28,26)$ | 5476 |
| $F_{P_{B,o}}$ | $(9,27,25)$ | 4547 |
| $F_{N_1}$ | $(5,15,17)$ | 1074 |
| $F_{N_{B,e}}$ | $(9,25,23)$ | 3822 |
| $F_{N_{B,o}}$ | $(8,23,23)$ | 3340 |
| 原均值/normal 四次组合 | $(4,20,25)$ | 1910 |

没有倒置 $\beta$ 对 $\rho$ 的首项 $b_1$。它在此前 K 的局部图中可用，不是本条一般 L0 图的合法全局单位。

## 3. 准确饱和与有理单位门

原物理组使用此前原坐标的十一项非零分子

$$\rho,\lambda,w,w-1,R,C,\operatorname{num}\Delta,
\operatorname{num}Q,\operatorname{num}P_0,
\operatorname{num}(u-1),\operatorname{num}\ell.$$

已闭曲线组使用 $W,G,K,V,\alpha_0$，其中
$K=\operatorname{norm}\operatorname{Res}_\rho(\alpha_0,\beta_0)$，
$V=\operatorname{norm}\operatorname{lc}_\rho F_E$。这两个式子均从本源原方程重建，$V$ 精确匹配已证全文的 SHA。$G$ 采用其已完整返回的原明确公式。没有把 $\alpha_0$ 与其结式 $K$ 混为同一单位理由。

设两组乘积分别为 $S_{\rm physical},S_{\rm chart}$。加入两个辅助变量后，理想为

$$I=(\text{上表九行},\;\xi S_{\rm physical}-1,\;
\zeta S_{\rm chart}-1)\subset\mathbf Q[\xi,\zeta,\rho,w,\lambda].$$

每个剩余原解都映入这个理想的零集；单独证明 $I=(1)$ 因而足以关闭此原 L0 图。本条不预先声称该单位结论。

变量顺序固定 `(invPhysical,invChart,rho,w,lam), dp`。先在独立进程用 `liftstd(...,"std")` 检验最小单位输入，实际退出码 0、精确 marker、无 Singular `?` 诊断才写入完整输入。然后运行 `liftstd(I,cert,"slimgb")`，并实际乘回

$$\operatorname{matrix}(I)\,\mathrm{cert}=[1].$$

完整门限时 1200 秒、地址空间 8 GiB；只有上述乘回连同实际成功 marker、退出码 0 和无诊断，才算单位证书。无 `modstd` 或 parallel tasks。超时或只见 BEGIN 不排空。

## 4. 自含源和已实际构造

源：[2026-11-27-unit211-L0-full-original-paid-rho-leading-safe-slimgb-QQ-8542.py](../notes/2026-11-27-unit211-L0-full-original-paid-rho-leading-safe-slimgb-QQ-8542.py)。没有外部系数输入。

- Python 3.12.14、python-flint 0.9.0；参数 `--build-only`。
- 120 秒构造 alarm、8 GiB 地址空间；外部 150 秒硬限。
- 源 18086 字节，SHA-256 `fae9a57e1da69f192fd3dead3f3a7901ba8d2a091b77aefff4a06ee7c71b954d`。
- 实际退出码 0；外部墙钟 **4.752914 秒**、源内 **4.482696 秒**，最大 RSS **43072 KiB**。
- stdout 13498 字节，SHA-256 `22ad3909cd2e2ff241a4ef438cf09f537301697851e9bf01b1853fa6a9ef0d8e`。
- 生成完整 Singular 输入 753704 字节，SHA-256 `b2e3af026fc61f96cff84967ea4a87aa66410ce56f5961f3ca01a2ba3abd1feb`；可重算，不入库。
- [紧凑构造回执](../notes/2026-11-27-unit211-L0-full-original-paid-rho-leading-build-execution-8542.json)保留全部输入型及原单位身份。

公开专用 workflow `.github/workflows/invariant-subspace-L0-full-original-paid-leading-8542.yml` 随 source/workflow push 运行本输入一次。实际 run/job 与结果将另行登记。本地构造通过不构成一般 L0、Bell 真幂来源、算子桥或普通 ISP 的完成。
