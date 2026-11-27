# R150：L0 四个原八行子式与 X 的五曲线必要系统

日期：2026-11-27（台北时间）；会话：Astra-ISP-8542378f-20261127。AI-assisted GPT-6 Astra Pro。

**状态：完整原来源与新输入构造已验证；尚无单位证书。** 此次只对这份实质新输入启动一次完整 QQ 门。已经1200秒超时的旧 C/X/Y 系统保持冻结。

## 1. 五条原必要曲线

原九行系数矩阵及全部主元零纤维由[新增原子式](R150-appendix-essential-four-unit-two-plus-one-plus-one-L0-three-additional-original-parameter-curves.md)和[最初八行曲线](R150-appendix-essential-four-unit-two-plus-one-plus-one-L0-eight-by-eight-original-parameter-curve.md)完整支付。新源从原 Frobenius Gram 再生四个删行矩阵，逐条验证常数列 cofactor 的32项系数身份及原多项式组合，并只剥已付单位。

| 来源 | 曲线双次数 $(\deg_\lambda,\deg_w)$ | 项数 |
|---|---:|---:|
| 九行删7 | (39,53) | 1843 |
| 九行删8 | (39,54) | 1884 |
| 九行删5 | (40,53) | 1848 |
| 九行删2 | (40,54) | 1890 |
| 完整 $\operatorname{Res}_\rho(F_E,F_N)$ 后的 X | (34,52) | 1580 |

各曲线的精确SHA与前稿一致并在源码中逐一核验。这份输入使用四个原子式与 X；没有再次执行旧高次 Y 的三曲线门，也没有读取 scratch 系数缓存。

## 2. 仅用已付的纯参数单位

旧原图给十个纯参数单位：$\lambda,w,w-1,R,C_{\rm mom},P_{0,\rm num},W,G,K,V$。新[整个 X 的 lambda 首项返回](R150-appendix-essential-four-unit-two-plus-one-plus-one-L0-X-lambda-leading-complete-exclusion.md)另已完整支付 $w+1,2w+1,H_7(w)$，该自含证明的源SHA为 `579c3c755b7356598085dd1577a9951736c85f6ada1e8e6e4346e1f02f0d5029`。

令这13个单位的乘积为 $S$，五条原曲线依次为 $C_7,C_8,C_5,C_2,X$。在

$$
\mathbb Q[z,w,\lambda]
$$

中采用必要理想

$$
I=(C_7,C_8,C_5,C_2,X,zS-1).
$$

每个原解都使13单位非零，故可令 $z=S^{-1}$ 而成为本理想的零点。遗漏含 rho 的其他物理单位只会扩大此必要系统，不会删去原解。这里没有倒置任何未知曲线或余式首项。

## 3. 构造与完整证书标准

- 自含源：[2026-11-27-unit211-L0-five-original-minors-parameter-curves-safe-slimgb-QQ-8542.py](../notes/2026-11-27-unit211-L0-five-original-minors-parameter-curves-safe-slimgb-QQ-8542.py)。
- 源23272字节，SHA256 `f48568e06e13d777e0649fb7e8f5f1720a35823d4be853a22c10d034ac54887d`。
- 实际 `--build-only`：70.484423426秒、RSS114280 KiB、exit0。
- 三变量、五个非饱和生成元、13个已付单位；完整 Singular 输入394463字节，SHA256 `230f4b911f6d93f32bfa45de9b414d33b70bca03ee70809a040ad1423d548491`。
- 源构造alarm300秒、外部硬限310秒、地址空间8GiB。
- stdout29423字节，SHA256 `ed22eae99a42b03e3681d225cbd2a2d710948cb966ca397e3ded88209ea49067`。
- [构造小回执与五条原曲线轮廓](../notes/2026-11-27-unit211-L0-five-original-minors-parameter-curves-build-execution-8542.json)。

专用 workflow `.github/workflows/invariant-subspace-L0-five-original-minors-8542.yml` 从冻结提交部分克隆，实际 pull 后检查两个 README；先用独立 std 实例核工具，再仅对此新 I 执行1200秒 QQ slimgb。完整结论必须同时有正常退出、没有 Singular 诊断、返回基为1以及实际

$$
\operatorname{matrix}(I)\,\mathrm{cert}=[1].
$$

构造通过、模支持或任何尚未返回的运行状态都不作一般 L0 排除。

## 实际门返回：输入冻结

run45918826850 / job140244380823 于2026-11-27 01:09:29 UTC完成。独立std测试成功，完整slimgb QQ门在1200秒超时，只输出 `ISP_L0_BEGIN_FIVE_MINORS_QQ_LIFT`；无单位、无lift乘回。driver实际1268.484761秒、4159892KiB、source exit1。原输入394463字节/SHA230f4b91保持，冻结不重跑。CI实际pull并检查两README于00:48:18.443368 UTC，已读提交029dfddea1d7b5418e83bf75fdbb5350de2e146d；两规则blob均无变。完整小回执见 `notes/2026-11-27-unit211-L0-five-original-minors-actual-QQ-timeout-8542.json`。继续新的原一元覆盖返回。
