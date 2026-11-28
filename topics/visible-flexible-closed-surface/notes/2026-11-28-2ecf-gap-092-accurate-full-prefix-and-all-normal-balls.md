# 间隙 23/25 新物理图的全前缀度量、曲率及全部近点

**准确有理与有向区间证明。** [R267](../results/R267-new-gap-092-full-physical-prefix-metric-and-reach.md) 对新实际源重新计算全部 64 格、完整新 Γ95 端口/真实 coast 及出口。各自重生的局部物理格回执由总报告的 SHA 列表绑定。原内格与准确末格的整个度量谱误差上界分别为 2.324067e−10 和 4.967728e−10，最大自身曲率低于 7.599878。含中央、反射、真边界的整个有边紧集 reach≥5/38。以下命令先按 [gap.92 新 Cauchy H65 和 Γ95 物理生成记录](2026-11-28-2ecf-gap-092-physical-cauchy-65-and-gamma95.md)形成两份新 master，不使用原 gap1.05 的任何数值上界。新 PVA 九项差、真部分弧长 primitive、完整所有内格和整圈高度及精确分数路径/球半径的每一子进程均自然返回 0。

## 可移植重生

在运行目录 W 中执行。S 是公开课题 scripts 的绝对路径，E 是同次物理 IVP 采样产生 ramp-33.npz 与 ramp-65.npz 的目录。先按原记录产生 G10/G11 的原材料与原 5292 第 9 态。原命令只将脚本及 master 的位置换成这三个变量。

```sh
cd "$W"
export OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 OMP_NUM_THREADS=1
python3 -u "$S/2ecf-polar-new-gap-terminal-input.py" --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --master-report polar-new-gap-092-master.json --prefix polar-gap092-certificate
python3 -u "$S/2ecf-polar-new-gap-terminal-port.py" --scripts-dir "$S" --master polar-gap092-certificate-endpoint-submaster.npz --coast-master polar-new-gap-092-master-coast.npz --master-report polar-new-gap-092-master.json --gram-report polar-gap092-certificate-endpoint-input.json --angular-cells 2048 --output polar-gap092-full-port.json
python3 -u "$S/6a65-geometry-final-ramp-port-primitive.py" --master polar-gap092-certificate-endpoint-submaster.npz --coast-master polar-new-gap-092-master-coast.npz --gram-report polar-gap092-certificate-endpoint-input.json --port-report polar-gap092-full-port.json --port-source "$S/2ecf-polar-new-gap-terminal-port.py" --scripts-dir "$S" --output polar-gap092-full-primitive.json
python3 -u "$S/2ecf-polar-new-gap-raw-ramp-certificate.py" --scripts "$S" --master polar-new-gap-092-master-ramp.npz --submaster polar-gap092-certificate-endpoint-submaster.npz --master-report polar-new-gap-092-master.json --coast polar-new-gap-092-master-coast.npz --endpoint-input polar-gap092-certificate-endpoint-input.json --stage interior --out polar-gap092-certificate-first63.json
python3 -u "$S/2ecf-polar-new-gap-raw-ramp-certificate.py" --scripts "$S" --master polar-new-gap-092-master-ramp.npz --submaster polar-gap092-certificate-endpoint-submaster.npz --master-report polar-new-gap-092-master.json --coast polar-new-gap-092-master-coast.npz --endpoint-input polar-gap092-certificate-endpoint-input.json --stage terminal --terminal-trace polar-gap092-full-primitive.json --out polar-gap092-certificate-terminal.json
python3 -u "$S/2ecf-polar-new-gap-exit-graph.py" --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --trace polar-gap092-full-primitive.json --endpoint-input polar-gap092-certificate-endpoint-input.json --cells 1024 --output polar-gap092-exit-graph.json
python3 -u "$S/2ecf-polar-new-gap-prefix-reach.py" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --first polar-gap092-certificate-first63.json --last polar-gap092-certificate-terminal.json --port polar-gap092-full-port.json --trace polar-gap092-full-primitive.json --graph polar-gap092-exit-graph.json --endpoint polar-gap092-certificate-endpoint-input.json --output polar-gap092-entire-prefix-reach.json
```

## SHA256

| 原件 | SHA256 |
|---|---|
| 2ecf-polar-new-gap-terminal-input.py | 63adc4006eeedcaf96a1454e07dfacc12cc285ebbd88f9de27ea63dbbba7705c |
| 2ecf-polar-new-gap-terminal-port.py | f045d7844a3a23d256a4dda9a8a9fdced39074d52c7268996dc891258b9864d0 |
| 2ecf-polar-new-gap-raw-ramp-certificate.py | 0819c15ebfe99e39a5ff1acfee455b3595b84784b0ec91b54af89c74e1c1ae7f |
| 2ecf-polar-new-gap-exit-graph.py | 9f246895c0c8a7253eb3b20fb5c27b298269191ae1d7fa31f06f483a04b7aabe |
| 2ecf-polar-new-gap-prefix-reach.py | 9454293ed169114db0174866e079501641a1f501e0c2a673eda40639df2456f4 |
| polar-gap092-full-port.json | 06edf191dc2d16a98a8e62219831135c4c4ce9b80607aee8be8b266d24a91d85 |
| polar-gap092-full-primitive.json | b1a3d2e5c7c20ab1b4c00b403c76ce6e22409401dd64626d55dd7a995ecd9ec9 |
| polar-gap092-certificate-first63.json | d098e24ae62c5ec1ef7b9276dfe847608f2cd88283031070c90a56391ec85657 |
| polar-gap092-certificate-terminal.json | 21136f66f523998b88b5ccc1c17db0d14a88f41616858984215f951daaa6c8bd |
| polar-gap092-exit-graph.json | 26f867e47cf77153276bfc37f516083180e02e546d9d2df1b17cd8b06f7c5874 |
| polar-gap092-entire-prefix-reach.json | cdf47a7f031f879f1d80bd8b1c6eb03a674abd8effd14801e53f94e6416ead4b |
| polar-gap092-certificate-endpoint-input.json | 5b63b025716f16e4206a2bdbb61da3b49ae8f8f78b0ba273dfa3a179f520194f |
| polar-gap092-certificate-endpoint-submaster.npz | 234fd5fd5b78c1e44431f107bed22b1b7c91ac3b720723d1be99c8a810f9f600 |
| polar-gap092-primitive-terminal-graph-driver-exit.json | 066930abb507138bfa6bd442d1c361f30ac57d89d746a9a7b784a32797351183 |
| polar-gap092-certificate-prepare-exit.json | fb86d2563cd4b084b682a520aa8bb4ebabfbdbd70a819b874ee89a863d4d81eb |
| polar-gap092-certificate-prepare.log | 99afb6db64bfc9a616f769133765b42663215dc5fcea968bfe73fb8f662e115b |
| polar-gap092-full-port-exit.json | 43c9d5bb601caf7267a1c35eafe30d894878615f7a7f6fce843a4d053aec6e2b |
| polar-gap092-full-port.log | 9f488af27d6ea0e41607bf49be4747bbc1ec4ccd76622863290c942f9d3f20c9 |
| polar-gap092-full-primitive-exit.json | 77ffd545905030b3c2d4897c9e8ee8523d04264a987ad708264d68104841ed8c |
| polar-gap092-full-primitive.log | 35a88304908de744c8a39bbc73e02b5393aad5d0c0942197ac0c0b1408be5328 |
| polar-gap092-certificate-first63-exit.json | e385c9ffcd81bba8d1e69b2fe5bda09a3e7d93282de6bd8561427df6c88528ef |
| polar-gap092-certificate-first63.log | 6c80fdddaa414d72587857164cf8db779a16402e565fec8883f8e8d57b40f416 |
| polar-gap092-certificate-terminal-exit.json | 0d5a26ca003665ac8cc550b71eb799c3bd21527502edf31ca9a4fc335a24bee6 |
| polar-gap092-certificate-terminal.log | cb8becb27ad1c1eedbf40a919e5bb1e699c96bb0471f920ea1846659f8cdb732 |
| polar-gap092-exit-graph-exit.json | ee75295408b28d0dfc8625670859e32b45429d86966a06e97ee82f2db664631a |
| polar-gap092-exit-graph.log | c332210f84683c147388bd75aacd29e742371dddc9e84186b9a35deb59d91cf4 |
| polar-gap092-entire-prefix-reach-exit.json | 3b495fae026b3b3326703692a6b4218f41e03d42460bc5b5a36f365014813024 |
| polar-gap092-entire-prefix-reach.log | c15daf37cd1b20e09a4970e67e399082a0f775ed6221f394484b2d91a6c1f4c0 |
