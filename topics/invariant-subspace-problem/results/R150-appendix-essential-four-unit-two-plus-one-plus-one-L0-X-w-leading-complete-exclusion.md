# R150：L0 原 X 的整个 w 首项零面排除

日期：2026-11-27（台北时间）。会话：Astra-ISP-8542378f-20261127；AI-assisted GPT-6 Astra Pro。

**状态：已证明。** 在原非零均值 L0 图上，$X(\lambda,w)$ 的 w 首项不为零；整个 $\lambda=3/2$ 纤维和四次首项曲线均已返回原约束排除。此前独立的 lambda 首项排除继续有效。这里不宣称整个 L0 为空。

## 1. 原必要曲线和准确首项

沿用[原八行 cofactor 曲线](R150-appendix-essential-four-unit-two-plus-one-plus-one-L0-three-additional-original-parameter-curves.md)的删行7曲线 $C$，以及原 $P_1$ 返回后的 $E1,N1$ 对 rho 的完整结式 $X$。二者的 $(\lambda,w)$ 次数为 $(39,53)$、$(34,52)$。

本次自含源从原 Gram 和正确双点乘法重新构建全部输入，逐列核对八阶 cofactor 及原行组合，再剥除已独立支付的原单位。准确多项式身份为：

- C SHA256：`6057a487720992327d9e065ec6b7ef5e54896637f1c756a28391fd734737b50c`；
- X SHA256：`519fe7c69a0cf7c05283aa66833331b64e7654bb6ec0daec606c49b2c2a02f68`。

设
$$J_4(\lambda)=16\lambda^4-52\lambda^3+42\lambda^2-3\lambda+1.$$
源实际验证整个多项式身份
$$\boxed{\operatorname{lc}_wX=-\frac{\lambda^5(2\lambda-3)^2J_4(\lambda)^2}{5804752896}.}\tag{1}$$
原非零孤立均值已给 $\lambda\ne0$。其余两个因子没有预先倒置，分别处理如下。

## 2. 整个 lambda=3/2 纤维

把同一个 C、X 代入 $\lambda=3/2$，得到 QQ[w] 中完整的 52、51 次多项式。实际扩展 Euclid 给
$$a(w)C(3/2,w)+b(w)X(3/2,w)=1,\qquad(\deg a,\deg b)=(50,51).\tag{2}$$
两乘积及和准确回乘，系数对 SHA256 为
`ec89a2d1b010ed9b67e0a533e33fc7ff011da44f405ed575972960d1d88192f2`。
未除任何特殊化后的 w 首项或选择 w 根；故整个原纤维为空。

## 3. J4 的完整 QQ 覆盖

形成完整 QQ Sylvester 结式
$$R(w)=\operatorname{Res}_{\lambda}(C,J_4).$$
实际 $\deg R=208$，SHA256 为
`3084b6cc670e41ed38aed1f1e449c3e17162a8f31e960c99e74d4a25ded1ea6d`。
不剥任何 w 因子。任意原 C=J4=0 的点，其 w 都在这个实际完整一元覆盖中；参数特殊化导致首项降次也包含在结式的零集合内。

取素数 1009。R 的有理首项约化非零，其单首项化后的全部系数属于 $\mathbb Z_{(1009)}$。另一方面，X、J4 的原 lambda 次数 34、4 在模 1009 下都保持，故完整模结式正是
$$\overline S(w)=\overline{\operatorname{Res}_{\lambda}(X,J_4)}.$$
其次数为 204，SHA256 为
`c161af07755078cc1ebd2b304304c74889ab1bf92bd9d6772a13b64f7b3967e1`。

实际两乘积回乘给
$$A\overline R+B\overline S=1,\qquad(\deg A,\deg B)=(203,207).\tag{3}$$
系数对 SHA256 为
`95102cbe3a2df79a4a2fef4b72f2819462d77edf011b7ea6329a116804d008f2`。

若 R、S 在特征零中有共同复根，其单首项 QQ 最小多项式整除单首项且 1009 整的 R，Gauss 引理使它同样属于 $\mathbb Z_{(1009)}[w]$。它模 1009 仍有正次数，并整除两个模结式，违反 (3)。因此整个 J4 曲线不能含原 C=X=0 的点。这里返回的是完整实际一元 QQ 覆盖，不是从多变量模单位直接推出特征零空集。

## 4. 已付环和实际回执

由 (1)--(3)，原图现可合法支付 $2\lambda-3,J_4$，X 可在该已付局部化环中首一化为 w 的 52 次式。源逐项检查首项的全部因子已付，并回乘 $X/\operatorname{lc}_wX$ 的有理表示身份。先前[完整 lambda 首项排除](R150-appendix-essential-four-unit-two-plus-one-plus-one-L0-X-lambda-leading-complete-exclusion.md)仍给 lambda 的 34 次首一化；两者都不允许倒置任意新余式的首项。

源：`notes/2026-11-27-unit211-L0-X-w-leading-complete-original-return-8542.py`。

- 源 SHA256：`54f6780f1f7fcbd4d2b0f2438a90836ff223cfc47e284805476c7fbef4b47d35`，19396 字节；无需外部系数缓存。
- 实际 exit 0，墙钟 **21.511314 秒**，RSS **96348 KiB**；上限 180 秒、外部190秒、4 GiB。
- stdout 17424 字节，SHA256 `0ac57575ac740fe27f13991dd1775c37cd8c2f40125d4704a28bc14aba09385d`。
- 小回执：`notes/2026-11-27-unit211-L0-X-w-leading-complete-execution-8542.json`。

剩余一般 L0 仍须返回同一 rho、t 的原最高式与全部 P/N；本条只关闭准确指定的整个首项零面。
