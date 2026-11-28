# 同一大 gap 中央下改变坡度的实际 H65 输入

将 [R281](../results/R281-positive-support-central-cylinder-at-full-gap.md) 的支持半径取为两个新的有理例子。长短轴、半宽差与中央 reach 皆由该文的全角解析公式得到。每套中央在原 $v=.045$ 与另一条新坡度各做一次独立的真实 191 模式 H65 积分，材料坡度变化会更换 ramp 和 coast 的真实度量及位置。真实 Γ95 由相应末圈生成，未沿用原椭圆或另一组 ramp。

| $p,r$ | 精确公式给出的 $A$ | $B$ | $A-B$ | 中央最小曲率半径 | $v$ | H65 节点 metric | H65 节点曲率 | H65 最小 $n$ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 16, 21/100 | 1.43227170 | 0.38105684 | 1.05121485 | 0.210 | 0.045 | 3.52488e-12 | 10.844707032 | 0.168857615 |
| 16, 21/100 | 1.43227170 | 0.38105684 | 1.05121485 | 0.210 | 0.0225 | 3.54397e-12 | 5.401027594 | 0.170797815 |
| 32, 1/4 | 1.41907008 | 0.36614332 | 1.05292676 | 0.250 | 0.045 | 2.71511e-12 | 14.467956646 | 0.126257143 |
| 32, 1/4 | 1.41907008 | 0.36614332 | 1.05292676 | 0.250 | 0.012 | 2.32334e-12 | 4.000000000 | 0.128216378 |

以上 H65 数值每例有 65 个完整原生径结点和 768 个实际角。原 $v=.045$ 的两例即使中央曲率下降，ramp 仍分别到 10.84 与 14.47。减小真实坡度后峰值显著降低。$p=32$ 的初始 Fourier 截断在曲率 $1/\rho$ 上约 $1.99\cdot10^{-11}$；没有从有限原生积分推出整个 ramp 的严格 metric 或 reach。

使用主题 scripts 目录 `S`，沿用 R281 的程序和新可选坡度程序，两者均保存新的独立物理主文件。

```bash
python "$S/2ecf-strong-stadium-support-physical-H65.py" --scripts "$S" --power 16 --offset 21/100 --prefix stadium-p16r21-H65
python "$S/2ecf-strong-stadium-support-variable-H65.py" --scripts "$S" --power 16 --offset 21/100 --slope 0.0225 --prefix stadium-p16r21-v0225-H65
python "$S/2ecf-strong-stadium-support-physical-H65.py" --scripts "$S" --power 32 --offset 1/4 --prefix stadium-p32r25-H65
python "$S/2ecf-strong-stadium-support-variable-H65.py" --scripts "$S" --power 32 --offset 1/4 --slope 0.012 --prefix stadium-p32r25-v012-H65
```

各自真实 ramp、Γ95 文件的 SHA-256 如下。

- p16r21 为 `88fb84a209f6845372278d8bf306ed9f2314bec08245875d08deb0e7ec5a2c40` 与 `ebe1f6fc431e82641d468a2f024e5a005171e8456d5e1e25ff78b77e7f8a8373`。
- p16r21-v0225 为 `d0442bda87bb5456a1988be36a2676b06bd7879111dc7d47e3270cbfc6a070cc` 与 `6d3b56478e60e782476ae2e7cb47708d75fe7a281a23c13006dbe6b06b2127d5`。
- p32r25 为 `1aec2f2e5d4046f6db9cb324fced557db47151779eca8fe5910c6bdceab10df8` 与 `6f16cdef4daff9106ababd289aae88f5414df57f4ca2178e2f15a14c1c4da5f2`。
- p32r25-v012 为 `00aa860c47894e81ecc5991b14cc446f380bceb903ab45e5e6bd0f3fb2568bc1` 与 `978458636447335c6e00d542fdac538c5f27975b95ae92d56cc65d17ba6af502`。
